# Veda Technology Business & Service Management System

## 📌 Project Overview

The **Veda Technology Business & Service Management System** is a Python-based console application designed to manage different business and service-related activities of Veda Technology.

The system stores data in a **JSON file** and provides features for managing technology programs, digital services, training programs, internship programs, customer inquiries, and service requests.

---

## 🎯 Objectives

* Manage technology programs
* Manage digital services
* Manage training programs
* Manage internship programs
* Store customer inquiries
* Manage customer service requests
* Search records easily
* Generate a business summary report
* Store data permanently using a JSON file

---

## 🛠️ Technologies Used

* **Python**
* **JSON**
* **File Handling**
* **Object-Oriented Programming (OOP)**
* **Functions**
* **Lists and Dictionaries**
* **Exception Handling**
* **Date and Time Handling**

---

## 📂 Python Modules Used

```python
import json
import os
from datetime import datetime
```

### `json`

Used to read and write data in JSON format.

### `os`

Used to check whether the data file exists.

### `datetime`

Used to store the date and time when records are created.

---

## 💾 Data Storage

The project uses:

```text
veda_data.json
```

as its data file.

The system maintains six main categories:

1. Technology Programs
2. Digital Services
3. Training Programs
4. Internship Programs
5. Customer Inquiries
6. Service Requests

---

## ✨ Main Features

### 1. Technology Programs

Users can add and view technology programs.

Information stored includes:

* Program ID
* Program Name
* Department
* Duration
* Status
* Creation Date

Example ID:

```text
TP001
```

---

### 2. Digital Services

Users can add and view digital services.

Information includes:

* Service ID
* Service Name
* Category
* Description
* Status

Example ID:

```text
DS001
```

---

### 3. Training Programs

Users can manage training programs.

Information includes:

* Training ID
* Training Name
* Technology
* Duration
* Mode
* Status

Example ID:

```text
TR001
```

---

### 4. Internship Programs

Users can add and view internship opportunities.

Information includes:

* Internship ID
* Internship Title
* Technology
* Duration
* Stipend
* Status

Example ID:

```text
IN001
```

---

### 5. Customer Inquiries

Customers can submit inquiries.

Information includes:

* Inquiry ID
* Customer Name
* Email
* Subject
* Message
* Status
* Creation Date

Example ID:

```text
CI001
```

The default inquiry status is:

```text
Pending
```

---

### 6. Service Requests

Customers can create service requests.

Information includes:

* Request ID
* Customer Name
* Required Service
* Problem Description
* Priority
* Status
* Creation Date

Example ID:

```text
SR001
```

The default request status is:

```text
Open
```

---

## 🔍 Search Feature

The project provides a search option that searches across all stored records.

The user enters a keyword and the system checks the records for matching information.

Example:

```text
Enter search keyword: python
```

The matching records are then displayed.

---

## 📊 Business Report

The system can generate a business report showing the total number of:

* Technology Programs
* Digital Services
* Training Programs
* Internship Programs
* Customer Inquiries
* Service Requests

It also displays:

* Pending Customer Inquiries
* Open Service Requests

---

## 🆔 Automatic ID Generation

The project automatically generates unique IDs for records.

Examples:

```text
TP001
TP002
TP003
```

```text
DS001
DS002
DS003
```

```text
IN001
IN002
IN003
```

This avoids manually entering IDs.

---

## 🧩 Project Structure

```text
Veda-Technology-Management-System/
│
├── main.py
├── veda_data.json
└── README.md
```

> `veda_data.json` is automatically created when the program runs for the first time if it does not already exist.

---

## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

Check using:

```bash
python --version
```

### Step 2: Open the Project

Open the project folder in **VS Code**.

### Step 3: Run the Program

Open the terminal and execute:

```bash
python main.py
```

---

## 🖥️ Main Menu

The program provides the following menu:

```text
============================================================
       VEDA TECHNOLOGY MANAGEMENT SYSTEM
============================================================

1.  Add Technology Program
2.  View Technology Programs
3.  Add Digital Service
4.  View Digital Services
5.  Add Training Program
6.  View Training Programs
7.  Add Internship Program
8.  View Internship Programs
9.  Add Customer Inquiry
10. View Customer Inquiries
11. Add Service Request
12. View Service Requests
13. Search Records
14. Generate Business Report
0.  Exit

============================================================
```

---

## 🧠 Concepts Used

This project demonstrates several important Python programming concepts:

### Functions

Functions are used to divide the program into smaller and reusable parts.

Examples:

```python
load_data()
save_data()
generate_id()
get_required_input()
display_records()
```

### Classes and Objects

The main management functionality is implemented using:

```python
class VedaManagementSystem:
```

### File Handling

JSON file handling is used to permanently store data.

### Exception Handling

The program handles invalid JSON files and missing files.

### Lists and Dictionaries

Lists store multiple records, while dictionaries store individual record information.

### Loops and Conditions

Loops and conditional statements are used for menu handling, searching, validation, and report generation.

---

## 🔄 Program Flow

```text
Start
  ↓
Load JSON Data
  ↓
Display Main Menu
  ↓
Select Option
  ↓
Add / View / Search / Report
  ↓
Save Updated Data
  ↓
Return to Menu
  ↓
Exit
```

---

## 🔐 Data Validation

The project uses required-input validation to prevent empty values.

If the user enters an empty value:

```text
This field cannot be empty.
```

The program asks the user to enter the value again.

---

## 🚀 Future Improvements

The project can be further improved by adding:

* Login and authentication
* Admin dashboard
* Update and delete operations
* Email validation
* Database connectivity using MySQL
* GUI using Tkinter
* Web interface using Flask
* Export reports to PDF/Excel
* Better search and filtering
* Customer status tracking

---

## 👨‍💻 Author
Praval sharma

Developed as a Python-based management system project.

---

## 📄 License

This project is created for educational and project demonstration purposes.
