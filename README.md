# Sheen - Dental Clinics Management System

**Sheen** is a comprehensive management system designed specifically for dental clinics. It streamlines clinic operations, including patient management, appointment scheduling, and user administration.

## Table of Contents

- [Technologies](#technologies)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Technologies

- **Python**: Backend development
- **MySQL**: Database management
- **Flask**: Web framework
- **HTML/CSS**: Frontend development
- **JavaScript**: Interactive frontend elements
- **MySQL Connector**: Python-MySQL integration

## Features

- User Management: Create, update, and manage users (admins, staff).
- Patient Management: Register and manage patient records.
- Appointment Scheduling: Schedule, update, and view appointments.
- Command Interpreter: Test and manage backend operations through a command-line interface.
- Responsive Design: User-friendly interface accessible on various devices.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/sheen.git
    cd sheen
    ```

2. **Set Up Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up MySQL Database**:
    - Install MySQL server and start it.
    - Create a new database and user:
      ```sql
      CREATE DATABASE sheen_db;
      CREATE USER 'sheen_user'@'localhost' IDENTIFIED BY 'password';
      GRANT ALL PRIVILEGES ON sheen_db.* TO 'sheen_user'@'localhost';
      FLUSH PRIVILEGES;
      ```

5. **Configure Database Connection**:
    - Update `models/engine/db_storage.py` with your MySQL configuration.

6. **Initialize the Database**:
    ```bash
    python3 init_db.py
    ```

## Usage

1. **Run the Command Interpreter**:
    ```bash
    ./console.py
    ```

    - **Commands**:
        - `create <ClassName>`: Create a new instance of a class.
        - `show <ClassName> <id>`: Show the details of an instance.
        - `destroy <ClassName> <id>`: Delete an instance.
        - `update <ClassName> <id> <attribute_name> <attribute_value>`: Update an attribute of an instance.
        - `all <ClassName>`: Show all instances of a class.

2. **Run the Flask Application**:
    ```bash
    flask run
    ```

3. **Access the Web Interface**:
    - Open your web browser and go to `http://localhost:5000`.

## Project Structure

sheen/
├── models/
│ ├── init.py
│ ├── base_model.py
│ ├── user.py
│ ├── patient.py
│ ├── appointment.py
│ └── engine/
│ ├── init.py
│ └── db_storage.py
├── static/
│ └── styles.css
├── templates/
│ ├── base.html
│ ├── index.html
│ └── ...
├── console.py
├── init_db.py
├── app.py
└── README.md