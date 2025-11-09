# Employee Attendance System 🎯

<div align="center">

![Django](https://img.shields.io/badge/Django-5.0.6-green?logo=django)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.8.0-38B2AC?logo=tailwind-css)
![License](https://img.shields.io/badge/License-MIT-yellow)

A modern, QR code-based employee attendance system built with Django and Tailwind CSS. Simplify attendance tracking with automated ID card generation and real-time attendance monitoring.

[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoffee.com/mohsinraza)

</div>

---

## 📋 Table of Contents

- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
  - [Creating an Attendance Account](#1-creating-an-attendance-account)
  - [Adding Employees](#2-adding-employees)
  - [Marking Attendance](#3-marking-attendance)
  - [Viewing Attendance Records](#4-viewing-attendance-records)
- [Screenshots](#-screenshots)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)
- [Acknowledgements](#-acknowledgements)

---

## ✨ Features

- **QR Code-Based Attendance**: Employees can mark attendance by simply scanning their unique QR code
- **Automated ID Card Generation**: Professional ID cards with QR codes are automatically generated for each employee
- **Employee Management**: Easy-to-use admin interface for adding and managing employees
- **Attendance Dashboard**: Comprehensive view of all employee attendance records
- **Employee Search**: Quick search functionality to find specific employee records by name or email
- **ID Card Download**: Download individual or bulk employee ID cards
- **Responsive Design**: Beautiful, mobile-friendly interface built with Tailwind CSS
- **Secure Authentication**: Role-based access control with dedicated attendance accounts

---

## 🛠 Technology Stack

- **Backend Framework**: Django 5.0.6
- **Frontend**: Tailwind CSS 3.8.0
- **Database**: SQLite (default, configurable to PostgreSQL/MySQL)
- **QR Code Generation**: python-qrcode
- **QR Code Scanning**: HTML5-QRCode
- **Image Processing**: Pillow
- **Storage**: WhiteNoise (static files), AWS S3 (optional)
- **Additional**: Django Storages, Python-dotenv

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python**: 3.11 or higher ([Download Python](https://www.python.org/downloads/))
- **pip**: Python package manager (comes with Python)
- **Git**: Version control ([Download Git](https://git-scm.com/downloads))
- **Virtual Environment**: Recommended for dependency isolation

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mohsiniscoding/employee-attendance-django.git
cd employee-attendance-django
```

### 2. Create and Activate Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On Linux/MacOS:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser Account

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin credentials.

### 6. Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

---

## ⚙️ Configuration

### Environment Variables (Optional)

For production deployments with AWS S3 storage, create a `.env` file in the project root:

```bash
cp .env.example .env
```

Then configure the following variables:

```env
AWS_ACCESS_KEY=your_aws_access_key_id
AWS_SECRET_KEY=your_aws_secret_access_key
AWS_REGION_NAME=your_aws_region_name
AWS_BUCKET_NAME=your_s3_bucket_name
```

**Note**: AWS S3 configuration is optional. The system works with local file storage by default.

---

## 📖 Usage

### 1. Creating an Attendance Account

Before employees can mark attendance, you need to create a dedicated attendance account:

1. Navigate to the admin panel: `http://127.0.0.1:8000/admin`
2. Login with your superuser credentials
3. Go to **Users** → **Add User**
4. Create a new user (e.g., username: `attendance`, password: your choice)
5. After creation, edit the user and assign them to the `attendance_account_group`
6. Save the user

This account will be used at the attendance kiosk for scanning employee QR codes.

### 2. Adding Employees

1. Login to the admin panel: `http://127.0.0.1:8000/admin`
2. Click on **Employees** in the sidebar
3. Click the **Add Employee** button
4. Fill in the required fields:
   - First Name
   - Last Name
   - Designation
   - Email (must be unique)
   - Phone Number
   - Photo (JPEG format, max 2MB)
5. Click **Save**
6. The system will automatically generate an ID card with a unique QR code
7. Return to the employee list and click on the newly created employee
8. Click on the **ID Card Photo** link to download the generated ID card

### 3. Marking Attendance

1. Navigate to the login page: `http://127.0.0.1:8000/login`
2. Login using the attendance account credentials (created in step 1)
3. Allow camera access when prompted
4. Scan the employee's ID card QR code
5. Attendance will be marked automatically and a confirmation will be displayed

### 4. Viewing Attendance Records

1. Login to the admin panel: `http://127.0.0.1:8000/admin`
2. Click on **Attendance** in the sidebar
3. View all attendance records with timestamps
4. Use the search bar to filter by employee name or email
5. Export records as needed using Django's built-in admin features

---

## 📸 Screenshots

<details>
<summary>Click to expand screenshots</summary>

### Auto-Generated ID Card
<img src="https://i.postimg.cc/qMXVP9dX/image.png" alt="Employee ID Card" width="300">

### Attendance Account Login
![Attendance Login](https://i.postimg.cc/MH2N4YPF/image.png)

### QR Code Scanner Interface
![Mark Attendance](https://i.postimg.cc/9F2sYJq4/image.png)

### Attendance Confirmation
![Attendance Marked](https://i.postimg.cc/3xJ6PN1Y/image.png)

### Employee Management Dashboard
![Employee List](https://i.postimg.cc/28CXZyPh/image.png)

### Attendance Records
![Attendance List](https://i.postimg.cc/GpTMCyyw/image.png)

</details>

---

## 🗺 Roadmap

Future enhancements planned for this project:

- [ ] **CHECK-IN/CHECK-OUT System**: Implement separate check-in and check-out functionality (currently status shows as UNKNOWN)
- [ ] **Employee Reports**: Generate detailed attendance reports for individual employees
- [ ] **Date Range Reports**: Create reports for custom date ranges
- [ ] **Dashboard Analytics**: Add visual charts and statistics for attendance trends
- [ ] **Email Notifications**: Automated email alerts for absences or late arrivals
- [ ] **Mobile App**: Native mobile application for easier attendance marking
- [ ] **Biometric Integration**: Optional fingerprint or facial recognition support

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code follows the existing style and includes appropriate tests.

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](https://opensource.org/licenses/MIT) file for details.

---

## 👨‍💻 Author

**Mohsin Raza**
- Email: mohsin.doer@gmail.com
- GitHub: [@mohsiniscoding](https://github.com/mohsiniscoding)

If you find this project helpful, consider [buying me a coffee](https://buymeacoffee.com/mohsinraza) ☕

---

## 🙏 Acknowledgements

This project was built with the help of these amazing technologies:

- [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines
- [Tailwind CSS](https://tailwindcss.com/) - A utility-first CSS framework
- [HTML5 QR Code](https://github.com/mebjas/html5-qrcode) - Lightweight QR code scanner library
- [python-qrcode](https://github.com/lincolnloop/python-qrcode) - Pure Python QR Code generator
- [Pillow](https://python-pillow.org/) - The friendly PIL fork for image processing
- [Freepik](http://www.freepik.com) - ID card background resources

---

<div align="center">

**⭐ Star this repository if you find it helpful! ⭐**

Made with ❤️ by [Mohsin Raza](https://github.com/mohsiniscoding)

</div>
