# Vocallabs Outreach Pipeline

> Automated Company Discovery, Contact Discovery, Email Resolution, and Outreach Automation Pipeline

---

## Overview

Vocallabs Outreach Pipeline is a modular outbound lead generation and outreach automation system designed to streamline the process of discovering target companies, identifying key decision-makers, resolving professional email addresses, and executing personalized outreach campaigns.

This project was developed as part of the **Vocallabs / Subspace Software Development Engineer Internship Assessment**.

---

## Features

* Company Discovery
* Contact Discovery
* Email Resolution
* Automated Outreach
* JSON Export
* Logging & Monitoring
* Error Handling
* Retry Mechanism
* Unit Testing
* Modular Service-Oriented Architecture

---

## Architecture

```text
Input Domain
      │
      ▼
Company Discovery
      │
      ▼
Contact Discovery
      │
      ▼
Email Resolution
      │
      ▼
Deduplication
      │
      ▼
JSON Export
      │
      ▼
Email Generation
      │
      ▼
Email Delivery
```

---

## Project Structure

```text
vocallabs-outreach/
│
├── data/
│   ├── companies.json
│   ├── contacts.json
│   └── emails.json
│
├── logs/
│   └── pipeline.log
│
├── src/
│   ├── config/
│   │   └── settings.py
│   │
│   ├── models/
│   │   ├── company.py
│   │   ├── contact.py
│   │   └── email.py
│   │
│   ├── services/
│   │   ├── ocean_service.py
│   │   ├── prospeo_service.py
│   │   ├── eazyreach_service.py
│   │   └── brevo_service.py
│   │
│   ├── pipeline/
│   │   └── outreach_pipeline.py
│   │
│   ├── utils/
│   │   ├── logger.py
│   │   ├── dedupe.py
│   │   ├── retry.py
│   │   ├── file_exporter.py
│   │   └── email_templates.py
│   │
│   └── main.py
│
├── tests/
│   ├── test_ocean.py
│   ├── test_prospeo.py
│   └── test_pipeline.py
│
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

## Technology Stack

| Category        | Technology    |
| --------------- | ------------- |
| Language        | Python 3      |
| Validation      | Pydantic      |
| Configuration   | python-dotenv |
| Logging         | Loguru        |
| Testing         | Pytest        |
| Storage         | JSON          |
| Version Control | Git & GitHub  |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Vocallabs_Subspace_assignment.git

cd Vocallabs_Subspace_assignment
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file:

```env
OCEAN_API_KEY=

PROSPEO_API_KEY=

EAZYREACH_API_KEY=

BREVO_API_KEY=

BREVO_SENDER_EMAIL=

BREVO_SENDER_NAME=
```

---

## Running The Pipeline

```bash
python src/main.py
```

Example:

```text
Enter Company Domain: google.com
```

Output:

```text
Companies Found: 5

Emails Found: 10

Pipeline Complete
```

---

## Generated Outputs

### Companies

```text
data/companies.json
```

### Contacts

```text
data/contacts.json
```

### Emails

```text
data/emails.json
```

### Logs

```text
logs/pipeline.log
```

---

## Testing

Run all tests:

```bash
pytest
```

---

## Engineering Decisions

### Service Layer Architecture

Each external integration is isolated behind a dedicated service:

* OceanService
* ProspeoService
* EazyreachService
* BrevoService

This makes the system:

* Maintainable
* Extensible
* Testable
* Easy to replace with production APIs

---

### Error Handling

The pipeline continues processing even when a specific company fails.

Benefits:

* Improved reliability
* Better fault tolerance
* Reduced pipeline interruptions

---

### Retry Mechanism

Transient failures are automatically retried before marking a request as failed.

Benefits:

* Increased robustness
* Better API reliability
* Improved production readiness

---

### Logging

Execution logs are written to:

```text
logs/pipeline.log
```

Logged events include:

* Pipeline Start
* Company Discovery
* Contact Discovery
* Email Generation
* Pipeline Completion
* Errors & Exceptions

---

## Future Improvements

### Integrations

* Ocean.io
* Prospeo
* Eazyreach
* Brevo

### Scalability

* Async Processing
* Message Queues
* Worker Pools
* Database Persistence
* Distributed Execution

### Analytics

* Campaign Tracking
* Email Open Rates
* Click Tracking
* Conversion Tracking

---

## Assignment Notes

Due to third-party platform access limitations during development, service implementations currently use mock discovery and enrichment layers while preserving production-ready interfaces.

The architecture is intentionally designed so that mock implementations can be replaced with live APIs without changing the orchestration layer.

---

## Author

**Praveen**

