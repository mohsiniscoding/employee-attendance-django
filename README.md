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
Auto-generated ID Card

<img src="https://private-user-images.githubusercontent.com/38476853/331842860-816952b5-0bb5-48db-a620-18c29052cdb6.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTYwODU4NDIsIm5iZiI6MTcxNjA4NTU0MiwicGF0aCI6Ii8zODQ3Njg1My8zMzE4NDI4NjAtODE2OTUyYjUtMGJiNS00OGRiLWE2MjAtMThjMjkwNTJjZGI2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MTklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTE5VDAyMjU0MlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTAzNjVkZTA1NWE2NTJkNDk5MzllNDAwODkzMzMzMjFlMDZiZjkzZmQ0M2M1OGNjZjFkZTVkYWQ2YmUzZjJmM2EmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.ZepldW5TFkrSvYtmVgN4IxDoP5la0luUQ-6eIhx_4D4" width="200">

Attenance account login
![image](https://private-user-images.githubusercontent.com/38476853/331843029-f6bdc734-cc0a-4340-81d5-4d3de06fde73.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTYwODYwMzEsIm5iZiI6MTcxNjA4NTczMSwicGF0aCI6Ii8zODQ3Njg1My8zMzE4NDMwMjktZjZiZGM3MzQtY2MwYS00MzQwLTgxZDUtNGQzZGUwNmZkZTczLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MTklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTE5VDAyMjg1MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTJhZjQyNjcyMTk2Mzk0OWMzMGNhNWNmYzEwZWJhNjIyNWI5ZDZkY2IzZTcxNzFmNDMyMmI3NzUxMmMwY2M4MzMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.c-LrSvpRRqLKKws1POYKd8wK4yTfpKpRqnTOxlgAgw0)

Mark Attendance
![image](https://private-user-images.githubusercontent.com/38476853/331843033-00052262-bf4f-4556-acd8-050eec390041.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTYwODYwMzEsIm5iZiI6MTcxNjA4NTczMSwicGF0aCI6Ii8zODQ3Njg1My8zMzE4NDMwMzMtMDAwNTIyNjItYmY0Zi00NTU2LWFjZDgtMDUwZWVjMzkwMDQxLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MTklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTE5VDAyMjg1MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdkNWY1MzA3MDUxNDRkZjA4NTUwMzBkNGYyMTk2YWYxNWIzMGI1MGFjMWIxODliODA4ZjQ0NDNjMWM1NWFkM2QmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.86xV_Z-hKPcOzHM03l52xPLRB_SA2E0gY9nqDcwbMVM)

Attendance Marked
![image](https://private-user-images.githubusercontent.com/38476853/331843034-062c1ccd-cd39-42b0-a84e-b7adacc82eef.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTYwODYwMzEsIm5iZiI6MTcxNjA4NTczMSwicGF0aCI6Ii8zODQ3Njg1My8zMzE4NDMwMzQtMDYyYzFjY2QtY2QzOS00MmIwLWE4NGUtYjdhZGFjYzgyZWVmLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MTklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTE5VDAyMjg1MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTY2YTJlOTE2NThkZTUyYTc2ODU5YjQ4NTc4ODY1ZGI4OGNhNjg2NTNjNDc4NjQ2ZWE2MDNhODE4ZTQ1MTlkOTgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.sbrDIDjzkU65LQcYo0aR38vLYIEgfV4lsyL24RBHsaI)

Employee List
![image](https://private-user-images.githubusercontent.com/38476853/331843023-908bd7de-37bb-4aa0-899f-993e3ac58f5c.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTYwODYwMzEsIm5iZiI6MTcxNjA4NTczMSwicGF0aCI6Ii8zODQ3Njg1My8zMzE4NDMwMjMtOTA4YmQ3ZGUtMzdiYi00YWEwLTg5OWYtOTkzZTNhYzU4ZjVjLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MTklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTE5VDAyMjg1MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTVkOTg2ZWVlMjQ4NmY5MWNjYWRiMDgxYmQxZTU4ODg2NjQ2NzNiYTAzMmU2YzJmMDJjYjA4ZmJlOTI5YWUyMDUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.C5gorCJ6Uji6E3nmKDodWrVElM5jo3NtfYNCrCxpPpI)

Attendance List
![image](https://private-user-images.githubusercontent.com/38476853/331843026-be3537bf-fe1c-46c2-9054-630f4496029c.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTYwODYwMzEsIm5iZiI6MTcxNjA4NTczMSwicGF0aCI6Ii8zODQ3Njg1My8zMzE4NDMwMjYtYmUzNTM3YmYtZmUxYy00NmMyLTkwNTQtNjMwZjQ0OTYwMjljLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MTklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTE5VDAyMjg1MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTUxYmFhYmQzNzAwYzI0NTI0ZGViOGRmMTZmYTE0OTAwYzYxNTdiNjkzNDY2ODdkNjU0ZDVjOWM3MmY2ZWUzNzgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.SCzYoLO4NDCt6fQIdJ9DB7Bp1BwREVvhaFNeBFABelA)

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


