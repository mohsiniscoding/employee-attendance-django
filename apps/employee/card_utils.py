from PIL import Image, ImageDraw, ImageFont
from django.core.files.base import ContentFile
from django.conf import settings
from django.core.exceptions import ValidationError
import qrcode
import io
import os
import logging

logger = logging.getLogger(__name__)

def textsize(text, font):
    im = Image.new(mode="P", size=(0, 0))
    draw = ImageDraw.Draw(im)
    _, _, width, height = draw.textbbox((0, 0), text=text, font=font)
    return width, height

def get_id_card_photo(instance):
    logger.info(f'Generating ID card for {instance.first_name} {instance.last_name}')

    try:
        # Set the dimensions of the ID card
        card_width, card_height = (675, 1013)
        text_color = (255, 255, 255)

        # Open id_card_bg.jpg
        bg_path = os.path.join(os.path.dirname(__file__), 'data/id_card_bg.jpg')
        if not os.path.exists(bg_path):
            logger.error(f'ID card background image not found at {bg_path}')
            raise ValidationError('ID card background image not found. Please contact administrator.')

        id_card = Image.open(bg_path)
        draw = ImageDraw.Draw(id_card)

        # Load fonts
        bold_font_path = os.path.join(settings.BASE_DIR, 'fonts/Montserrat-Bold.ttf')
        if not os.path.exists(bold_font_path):
            logger.error(f'Bold font not found at {bold_font_path}')
            raise ValidationError('Required font files not found. Please contact administrator.')

        font = ImageFont.truetype(bold_font_path, size=40)

        # Validate employee photo exists
        if not instance.photo:
            logger.error(f'No photo found for employee {instance.email}')
            raise ValidationError('Employee photo is required to generate ID card.')

        # Add the employee photo to the ID card - horizontal center
        try:
            photo = Image.open(instance.photo)
            photo.thumbnail((240, 240))
        except Exception as e:
            logger.error(f'Error processing employee photo: {str(e)}')
            raise ValidationError(f'Error processing employee photo: {str(e)}')

        # Create a mask for a circular crop
        mask = Image.new('L', photo.size, 0)
        draw_mask = ImageDraw.Draw(mask)
        draw_mask.ellipse((0, 0, photo.size[0], photo.size[1]), fill=255)

        # Apply the mask to the photo
        circular_photo = Image.new('RGBA', photo.size)
        circular_photo.paste(photo, (0, 0), mask=mask)

        # Calculate coordinates to center the circular photo
        photo_width, photo_height = circular_photo.size
        x = (card_width - photo_width) // 2
        y = 95
        id_card.paste(circular_photo, (x, y), mask=circular_photo)

        ## Add the employee name, designation
        ## employee name
        full_name = f'{instance.first_name} {instance.last_name}'
        text_width, text_height = textsize(full_name, font)
        x = (card_width - text_width) // 2
        y = 350
        draw.text((x, y), full_name, text_color, font=font)

        ## employee designation
        regular_font_path = os.path.join(settings.BASE_DIR, 'fonts/Montserrat-Regular.ttf')
        if not os.path.exists(regular_font_path):
            logger.error(f'Regular font not found at {regular_font_path}')
            raise ValidationError('Required font files not found. Please contact administrator.')

        font_25 = ImageFont.truetype(regular_font_path, size=25)
        text_width, text_height = textsize(instance.designation, font_25)
        x = (card_width - text_width) // 2
        y = 400
        draw.text((x, y), instance.designation, text_color, font=font_25)

        ## Generate and add a QR code of the employee email
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(instance.email)
            qr.make(fit=True)

            qr_image = qr.make_image(fill_color="black", back_color="white")
            ## Resize the qr code
            qr_image = qr_image.resize((268, 268))

            ## Add the qr code to the card
            qr_code_width, qr_code_height = qr_image.size
            x = (card_width - qr_code_width) // 2
            y = 570
            id_card.paste(qr_image, (x, y))
        except Exception as e:
            logger.error(f'Error generating QR code: {str(e)}')
            raise ValidationError(f'Error generating QR code: {str(e)}')

        ## SCAN ME text
        font_20 = ImageFont.truetype(regular_font_path, size=20)
        text = 'SCAN ME'
        text_width, text_height = textsize(text, font_20)
        x = (card_width - text_width) // 2
        y = 560
        draw.text((x, y), text, (0,0,0), font=font_20)

        # Save the ID card to a BytesIO object
        output = io.BytesIO()
        id_card.save(output, format='JPEG', quality=85, optimize=True)
        output.seek(0)

        logger.info(f'Successfully generated ID card for {instance.first_name} {instance.last_name}')
        return ContentFile(output.read())

    except ValidationError:
        # Re-raise ValidationError to be handled by Django
        raise
    except Exception as e:
        logger.exception(f'Unexpected error generating ID card for {instance.email}: {str(e)}')
        raise ValidationError(f'Error generating ID card: {str(e)}')