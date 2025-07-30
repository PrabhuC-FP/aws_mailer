# 📧 Laravel AWS SES Email API (Using Python Script)

This Laravel controller (`AwsMailController`) lets you send emails via **Amazon SES** using a **Python script** backend. This is useful when you already have an AWS email sender script written in Python and want to reuse it in Laravel through an HTTP API.

---

## ✅ Features

- 🔁 Reuse existing Python-based AWS SES logic
- 🔐 Credentials from `.env`
- 📡 Simple HTTP API for sending emails
- 📄 JSON response
- 🔧 Easy to extend for attachments, templates, etc.

---

## 📦 Requirements

- Laravel 9 or 10
- Python 3 with `boto3` installed
- Verified sender email in AWS SES
- Composer + PHP 8+
- `aws/aws-sdk-php` for Laravel's SES support (future-proofing)

---

## 🛠️ Setup Instructions

### 1. Install Laravel (if not yet)

```bash
composer create-project laravel/laravel aws-mailer
cd aws-mailer
