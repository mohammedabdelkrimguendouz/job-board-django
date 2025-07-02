# Django Job Board Platform

A web-based job board platform built with Django. The application enables job seekers to apply for jobs and recruiters to post job listings. It features user authentication, profile management, job filtering, CV uploads, contact form, and REST APIs.

---

## 📌 Features

### 👥 User & Profile System (`accounts` app)
- **User registration, login, and logout**
- **Profile management:**
  - Image upload
  - City selection
  - Contact information
- **Edit profile:**
  - First name, last name
  - Email, phone number
  - Profile image

### 🧑‍💼 Job Board (`job` app)
- **Job operations:**
  - Add new job listings
  - List and view available jobs
- **Application process:**
  - Resume/CV upload (required)
  - Cover letter (optional)
  - Personal website link (optional)
- **Advanced filtering:**
  - By job title (search)
  - Job type (Full-time/Part-time)
  - Experience level
  - Job category
- **Pagination:** 3 jobs per page
- **Admin interface** for managing jobs and applications

### 🌐 REST API (`job` app)
- **API v1 (Function-Based Views):**
  - `GET /jobs/api/v1/jobs` - List all jobs
  - `GET /jobs/api/v1/jobs/<id>` - Get specific job details
- **API v2 (Class-Based Views):**
  - `GET /jobs/api/v2/jobs` - List all jobs
  - `GET /jobs/api/v2/jobs/<id>` - Get specific job details

### 📩 Contact Form (`contact` app)
- **Send messages with:**
  - Subject line
  - Email address
  - Message body
- **Email integration:**
  - Uses Gmail SMTP with `send_mail()`
