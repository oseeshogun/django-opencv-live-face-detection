# Vision PRO
================

A Django-based project for staff management and face recognition.

## Overview
-----------

Vision PRO is a web application designed to manage staff information and recognize faces using OpenCV. The project utilizes Django as the backend framework and provides a user-friendly interface for staff data management and face detection.

## Features
------------

* Staff data management: Create, read, update, and delete staff information
* Face recognition: Detect and recognize faces using OpenCV
* Training: Train the face recognition model using staff images
* Detection: Detect faces in real-time using the trained model

## Requirements
---------------

* Python 3.8+
* Django 5.1.1
* OpenCV 4.10.0.84
* NumPy 2.1.1
* Pillow 10.4.0

## Installation
------------

1. Clone the repository: `git clone https://github.com/oseeshogun/vision-pro.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Create a new Django project: `django-admin startproject visionpro`
4. Copy the [staff](cci:1://file:///Users/oseemasuaku/Documents/Projects/vision-pro/staff/models.py:14:0-16:53) app into the project directory
5. Run migrations: `python manage.py migrate`
6. Run the development server: `python manage.py runserver`

## Usage
-----

1. Access the staff management interface: `http://localhost:8000/`
2. Create a new staff member: `http://localhost:8000/staff/create/`
3. Train the face recognition model: `http://localhost:8000/training/`
4. Detect faces in real-time: `http://localhost:8000/detection/`

## Contributing
------------

Contributions are welcome! Please submit a pull request with your changes.

## License
-------

This project is licensed under the MIT License. See `LICENSE` for details.