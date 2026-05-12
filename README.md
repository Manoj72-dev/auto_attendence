# Automatic Attendance System

A Python-based desktop application for managing student attendance using **Face Recognition**. The project uses **Tkinter** for the graphical user interface, **OpenCV** for face detection and recognition, and **MySQL** for storing student and teacher data.

---

# Features

## Student Features

* Student registration and login
* Face dataset generation using webcam
* Automatic face recognition training
* Student profile management

## Teacher Features

* Teacher registration and login
* Face-based attendance monitoring
* View student information
* Attendance handling by section

## Face Recognition Features

* Webcam-based image capture
* Haar Cascade face detection
* LBPH Face Recognizer training
* Automatic classifier generation

---

# Technologies Used

* Python
* Tkinter
* OpenCV
* MySQL
* Pillow (PIL)
* NumPy

---

# Project Structure

```bash
auto_attendence-main/
│
├── main.py                               # Main login window
├── Std_Singin.py                         # Student registration
├── Student_Login.py                      # Student dashboard/login
├── Teacher_Login.py                      # Teacher dashboard/login
├── Tech_Singin.py                        # Teacher registration
├── traing.py                             # Face recognition training
├── haarcascade_frontalface_default.xml   # Haar Cascade model
├── classifier.xml                        # Generated trained model
├── data/                                 # Captured face images
└── README.md
```

---

# Requirements

Install Python 3.8 or above.

## Required Python Libraries

Install dependencies using:

```bash
pip install opencv-contrib-python pillow numpy mysql-connector-python
```

---

# MySQL Database Setup

Create a MySQL database named:

```sql
CREATE DATABASE new_schema;
```

Use the database:

```sql
USE new_schema;
```

---

# Create Required Tables

## Student Table

```sql
CREATE TABLE student (
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    uni_name VARCHAR(100),
    age INT,
    section VARCHAR(10),
    Roll_no INT,
    passward VARCHAR(50),
    Student_ID INT PRIMARY KEY,
    photosample VARCHAR(10)
);
```

## Teacher Table

```sql
CREATE TABLE teacher (
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    uni_name VARCHAR(100),
    age INT,
    passward VARCHAR(50),
    Gender VARCHAR(20),
    Teacher_ID INT PRIMARY KEY,
    section VARCHAR(10)
);
```

## Section A Table

```sql
CREATE TABLE seca (
    name VARCHAR(100),
    rollno INT,
    student_id INT
);
```

## Section B Table

```sql
CREATE TABLE secb (
    name VARCHAR(100),
    rollno INT,
    student_id INT
);
```

---

# Update MySQL Credentials

The project currently uses:

```python
host="localhost"
username="root"
password="@root@123"
database="new_schema"
```

If your MySQL credentials are different, update them in:

* `main.py`
* `Std_Singin.py`
* `Tech_Singin.py`
* `Student_Login.py`
* `Teacher_Login.py`

---

# How to Run the Project

## Step 1: Clone or Download the Project

```bash
git clone <repository-url>
```

Or extract the ZIP file.

---

## Step 2: Create Data Folder

Inside the project folder, create a folder named:

```bash
data
```

This folder stores captured face images.

---

## Step 3: Start MySQL Server

Make sure:

* MySQL service is running
* Database and tables are created
* Credentials are correct

---

## Step 4: Run the Application

```bash
python main.py
```

---

# How the System Works

## Student Registration

1. Student signs up
2. Student information is stored in MySQL
3. Webcam captures face images
4. Images are saved in the `data/` folder
5. Face recognition model is trained automatically

---

## Face Training

The `traing.py` file:

* Reads images from the `data/` folder
* Converts images to grayscale
* Extracts student IDs from filenames
* Trains the LBPH face recognizer
* Generates `classifier.xml`

---

## Attendance Process

Teachers can use the trained model to recognize students through webcam input and manage attendance.

---

# Important Notes

* Ensure your webcam is connected and accessible.
* The project requires proper lighting for accurate face detection.
* Keep `haarcascade_frontalface_default.xml` in the root project directory.
* Do not rename the `data` folder.
* OpenCV face recognition requires `opencv-contrib-python`.

---

# Common Errors and Fixes

## 1. ModuleNotFoundError

Install missing libraries:

```bash
pip install opencv-contrib-python pillow numpy mysql-connector-python
```

---

## 2. MySQL Connection Error

Check:

* MySQL server is running
* Username and password are correct
* Database exists

---

## 3. cv2.face Attribute Error

Install OpenCV contrib package:

```bash
pip install opencv-contrib-python
```

---

## 4. Webcam Not Opening

* Check camera permissions
* Close other apps using the webcam
* Restart the system if needed

---

# Future Improvements

* Email notifications
* Attendance reports export
* Improved UI design
* Password encryption
* Real-time attendance analytics
* Cloud database support
* Better face recognition accuracy

---

# Security Recommendations

Current project limitations:

* Passwords are stored in plain text
* Hardcoded database credentials
* No role-based authentication

Recommended improvements:

* Use hashed passwords
* Move credentials to environment variables
* Add proper authentication and validation
* Use prepared attendance logs

---

# Author

Automatic Attendance System using Python, OpenCV, Tkinter, and MySQL.

---

# License

This project is for educational and learning purposes.
