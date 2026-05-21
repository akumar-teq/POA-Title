# POA Title Automation System

## Project Overview

POA Title Automation System is an AI-powered title document processing platform designed for:
- Property title analysis
- OCR document extraction
- County record scraping
- Mortgage/lien classification
- Risk analysis
- PDF report generation

The system automates processing of county documents from Bexar County and similar public record websites.

---

# Tech Stack

## Frontend
- Next.js
- React
- Axios
- Tailwind CSS

## Backend
- FastAPI
- Python
- SQLAlchemy
- PostgreSQL

## OCR & AI
- Google Vision OCR
- Tesseract OCR
- Regex Extraction
- AI Parsing Engine

## Scraping
- Playwright

---

# Features

- Upload county PDF documents
- OCR text extraction
- AI field extraction
- Dynamic property search
- Bexar County scraping
- Risk classification
- PDF report generation
- Dashboard interface

---

# Project Structure

```bash
poa-title-system/
│
├── backend/
│   ├── app/
│   ├── storage/
│   ├── process_document.py
│   └── requirements.txt
│
├── frontend/
│   ├── app/
│   ├── components/
│   └── package.json
│
└── README.md
```

---

# Backend Setup

## Create Virtual Environment

```bash
python3 -m venv venv
```

## Activate Environment

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Backend

```bash
uvicorn app.main:app --reload
```

Backend URL:

```text
http://localhost:8000
```

---

# Frontend Setup

## Install Packages

```bash
npm install
```

## Run Frontend

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:3000
```

---

# OCR Setup

## Install Tesseract

```bash
sudo apt install tesseract-ocr
```

## Install OCR Packages

```bash
pip install pytesseract pdf2image pillow
```

---

# Playwright Setup

## Install Playwright

```bash
pip install playwright
```

## Install Browser

```bash
playwright install
```

---

# API Endpoints

## Upload PDF

```http
POST /upload
```

## Process Document

```http
POST /process
```

## Search Property

```http
GET /search/{query}
```

## Download Report

```http
GET /report
```

---

# Current Modules

- OCR Engine
- AI Extraction Engine
- Scraper Engine
- Risk Analysis
- PDF Reporting
- Frontend Dashboard

---

# Future Improvements

- AppLega Webhook Integration
- Advanced AI Extraction
- Multi-county Support
- Authentication System
- Cloud Deployment
- Queue Processing

---

# Author

POA Title Automation System
