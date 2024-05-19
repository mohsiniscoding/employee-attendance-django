[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoffee.com/mohsinraza)


# Employee Attendance System

This is a simple employee attendance system that allows employees to mark their attendance by scanning a QR code. The system is built using Django and Tailwind CSS.

## Features
* Employees can mark their attendance by scanning a QR code.
* Admins can view the attendance of all employees.
* Admins can add new employees.
* Admins can view the attendance of a specific employee.
* ID cards are automatically generated for each employee.
* Admins can download the ID cards of all employees.

## TODO
* Add the ability to allow CHECK-IN and CHECK-OUT. Currently, the system set status to UNKNOWN.
* Attendance report for a specific employee.
* Add the ability to generate a report for a specific date range.

## Screenshots

## Installation
Tested on Python 3.11

1. Clone the repository
```bash
git clone https://github.com/mohsiniscoding/employee-attendance-django.git
```

2. Change to the project directory
```bash
cd employee-attendance-django
```

3. Create a virtual environment
```bash
python -m venv venv
```

4. Activate the virtual environment
```bash
# Windows
venv\Scripts\activate

# Linux/MacOS
source venv/bin/activate
```

5. Install the dependencies
```bash
pip install -r requirements.txt
```

6. Run the migrations
```bash
python manage.py migrate
```

7. Create a superuser
```bash
python manage.py createsuperuser
```

8. Run the development server
```bash
python manage.py runserver
```

## Add Attendance account
We need to create an account for the Attendance app to mark attendance. To do this, we need to create a new user and assign the user to the `attendance_account_group`.

## How to use

### Adding a new employee
1. Login to the admin panel i.e. 127.0.0.1:8000/admin
2. Click on the `Employees` link
3. Click on the `Add employee` button
4. Fill first name, last name, and email, also add photo.
5. Click on the `Save` button
6. Go back to the `Employees` page and click on the employee you just added
7. Click on the link for `id card photo` to download the ID card

### Marking attendance
1. Go to the login page i.e. 127.0.0.1:8000/login
2. Login with the username and password of the Attendance account
3. Scan the ID card we generated in the previous step
4. The attendance will be marked

### Viewing attendance
1. Login to the admin panel i.e. 127.0.0.1:8000/admin
2. Click on the `Attendance` link
3. You will see the attendance of all employees
4. Use the search bar to search for a specific employee by name or email

## License
This project is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).

## Author
[Mohsin Raza] mohsin.doer@gmail.com

## Acknowledgements
* [Django](https://www.djangoproject.com/)
* [Tailwind CSS](https://tailwindcss.com/)
* [HTML5 QR Code](https://github.com/mebjas/html5-qrcode)
* [ID Card Background](http://www.freepik.com)


