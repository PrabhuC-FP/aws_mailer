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

pip install boto3
```

### 2. MENTION THE AWS KEY SECRET IN ENV FILE
```
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_DEFAULT_REGION=us-east-1
AWS_BUCKET=
AWS_USE_PATH_STYLE_ENDPOINT=false

```

### 3. RUN THE PROJECT
```
php artisan serv
```

### IMPORTANT!
- storage/python (Folder required with 2 major files)
- aws_mailer.py, send_mail.py (Required files used to send MAIL)

### END POINT
```
POST http://localhost:8000/api/send-aws-mail
```

```cURL
curl -X POST http://localhost:8000/api/send-aws-mail \
  -d "to=test@example.com" \
  -d "subject=Hello from SES" \
  -d "body=<h1>This is an email from Laravel using Python</h1>"
```
