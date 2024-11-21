# 🌐 **FastAPI Authentication Project**

A complete solution for managing users and their features using **FastAPI**, **SQLAlchemy**, **Alembic**, **JWT Authentication**, **PostgreSQL**, and cloud storage for images (S3-Compatible). This project is designed for easy deployment on **Liara** for automated operations.

---

## 🚀 **Features**

- **JWT Authentication**: Secure user authentication using JSON Web Tokens (JWT).
- **User Management**: User registration, login, email verification (OTP), profile updates, and avatar management.
- **Image Storage**: Secure upload and storage of user images in an S3-compatible cloud storage service.
- **Celery worker**: Send email to user with celery .
- **Docker Support**: Easily launch the project using Docker.
- **Database Migrations**: Use **Alembic** to manage and apply database changes.
- **Easy Deployment**: Deploy your project on **Liara** for hassle-free cloud hosting and scaling.

---

## 🛠️ **Installation & Setup**

### **Prerequisites:**

Before starting, ensure you have the following installed:

- **Python 3.10** or higher
- **PostgreSQL 12** or higher
- **Docker** (for containerized deployment)
- **git** and **pip** for managing dependencies

---

### **1. Clone the Repository:**

Clone the project repository to your local machine:

```bash
git clone <repository-url>
cd <project-directory>
```

### **2. Set Up the Project with Docker:**
To start the project in a containerized environment using Docker, run the following command:
```bash
docker-compose up --build
```
This will automatically build the Docker images and start the project with all necessary dependencies.



### **3. Access the API Documentation:**
- **http://localhost:8000/docs#/** 

## 🌍 **Useful API Endpoints**
- **Register User**: [POST](http://localhost:8000/user/register) - Register a new user in the database.
- **Verify OTP**: [GET](http://localhost:8000/user/verify-otp?user_email=test56%40gmail.com&otp_code=549924) - Verify user with OTP sent to email.
- **Resend OTP**: [POST](http://localhost:8000/user/resend-code) - Resend the OTP if you lost the previous one.
- **User Login**: [POST](http://localhost:8000/user/login) - Log in after verifying OTP.
- **Logout**: [POST](http://localhost:8000/user/logout) - Logout the user.
- **Get Profile Info**: [GET](http://localhost:8000/profile/) - Retrieve the profile information of the authenticated user.
- **Edit Profile**: [PUT](http://localhost:8000/profile/edit/profile) - Edit the personal information in the user’s profile.
- **Upload Avatar**: [POST](http://localhost:8000/avatar/upload) - Upload a user avatar image.

### **4-Setting up a database with Alembic:**
To create migration files using Alembic, use the following command:
```bash
docker-compose exec app alembic revision --autogenerate -m "Initial migration"
```
Applying migrations to the database:
```bash
docker-compose exec app alembic upgrade head
```

## 📁 **Project structure **
app/
  models/        # Database models
  schemas/       # API input and output schemas
  crud/          # Services related to user management, authentication, and image uploading
  services/      # External services (e.g., email sending)
  main.py        # FastAPI main entry point
setting/         # Initial and required project settings
alembic/         # Database migration fileses



## ✍️ **Additional Description **
This project helps you easily implement complex authentication systems and communicate with the frontend via RESTful API.
The project can also easily scale to larger scales by using S3-compatible storage to store user images.
The database migration system with Alembic allows you to apply database structure changes automatically without having to stop the project