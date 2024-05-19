from PIL import Image, ImageDraw, ImageFont
from django.core.files.base import ContentFile
from django.conf import settings
import qrcode
import io
import os

def textsize(text, font):
    im = Image.new(mode="P", size=(0, 0))
    draw = ImageDraw.Draw(im)
    _, _, width, height = draw.textbbox((0, 0), text=text, font=font)
    return width, height

def get_id_card_photo(instance):
    print('Generating ID card for', instance.first_name, instance.last_name)

    # Set the dimensions of the ID card
    card_width, card_height = (675, 1013)
    text_color = (255, 255, 255)
    
    # open id_card_bg.jpg
    id_card = Image.open(
        os.path.join(
            os.path.dirname(__file__),
            'data/id_card_bg.jpg'
        )
    )
    draw = ImageDraw.Draw(id_card)
    
    # Load a font
    font = ImageFont.truetype(
        os.path.join(settings.BASE_DIR, 'fonts/Montserrat-Bold.ttf'),
        size=40
    )
    
    # Add the employee photo to the ID card - horizontal center
    photo = Image.open(instance.photo)
    photo.thumbnail((240, 240))

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
    font_25 = ImageFont.truetype(
        os.path.join(settings.BASE_DIR, 'fonts/Montserrat-Regular.ttf'),
        size=25
    )
    text_width, text_height = textsize(instance.designation, font_25)
    x = (card_width - text_width) // 2
    y = 400
    draw.text((x, y), instance.designation, text_color, font=font_25)
   

    ## generate and add a QR code 500x500 of the employee email
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
    qr.add_data(instance.email)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")
    ## resize the qr code
    qr_image = qr_image.resize((268, 268))

    ## add the qr code to the card
    qr_code_width, qr_code_height = qr_image.size
    x = (card_width - qr_code_width) // 2
    y = 570
    id_card.paste(qr_image, (x, y))

    ## SCAN ME text
    font_20 = ImageFont.truetype(
        os.path.join(settings.BASE_DIR, 'fonts/Montserrat-Regular.ttf'),
        size=20
    )
    text = 'SCAN ME'
    text_width, text_height = textsize(text, font_20)
    x = (card_width - text_width) // 2
    y = 560
    draw.text((x, y), text, (0,0,0), font=font_20)

    # Save the ID card to a BytesIO object
    output = io.BytesIO()
    id_card.save(output, format='JPEG')
    output.seek(0)
    
    return ContentFile(output.read())