# Web Login Brute Force Protection (Flask)

This project is a simple web-based login system built with Flask that demonstrates protection against brute force attacks.

Bu proje, Flask kullanılarak geliştirilmiş basit bir web giriş sistemidir. Brute force saldırılarına karşı koruma mekanizmaları içerir.

## Features

- IP-based login attempt tracking
- Account lock after multiple failed attempts
- Increasing delay system (anti-brute force)
- Simple web interface

## Technologies

- Python
- Flask

## Usage

1. Install Flask:
   pip install flask

2. Run the application:
   python app.py

3. Open in browser:
   http://127.0.0.1:5000/

## Security Note

This project is a basic simulation. Real-world systems require additional protections such as CAPTCHA, rate limiting, and monitoring systems.
