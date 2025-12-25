# Fake App Detection & Risk Analysis Platform

A web-based system for analyzing Android applications from the Google Play Store to assess the risk of impersonation or fraudulent behavior, with a focus on UPI, banking, and payment-related applications.

The platform supports both on-demand app analysis and a monitoring dashboard for flagged applications.

---

## Problem Statement

Fake and impersonator Android applications frequently misuse brand names and visual identities to deceive users, leading to financial fraud and data theft. Manual identification of such applications is inefficient and does not scale.

This project aims to automate the analysis of Play Store applications to detect impersonation signals and assign a meaningful risk level.

---

## Key Features

- User-friendly app scanning using Play Store URLs or app names
- No requirement to provide package names manually
- Ambiguity-safe resolution for generic or brand-level queries
- Heuristic-based risk scoring pipeline
- Separate modes for on-demand analysis and dashboard monitoring
- Robust handling of invalid inputs and third-party API failures
- Clean and professional web interface using Flask and Jinja templates

---

## System Architecture (High Level)

User Input (URL / App Name)
        |
Package Resolution
(URL extraction / Play Store search)
        |
Play Store Metadata Ingestion
        |
Feature Extraction
(Name similarity, brand detection, heuristics)
        |
Risk Scoring
        |
Result Presentation (Web UI)

---

## Technology Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, Jinja Templates  
- **Data Source:** Google Play Store (google-play-scraper)  
- **Text Similarity:** RapidFuzz  
- **Architecture:** Modular service-based design  

---

## Project Structure

Fake-App-Detector/
├── app/
│   ├── routes/        
│   ├── services/      
│   ├── templates/     
│   └── static/        
├── data/
│   ├── brands/        
│   └── raw/           
├── run.py
├── requirements.txt
└── README.md

---

## Application Workflow

1. The user opens the Scan App page.
2. The user enters a Play Store URL or an app name.
3. If the input is ambiguous, the system presents multiple candidate apps.
4. The selected application is analyzed using heuristic detection logic.
5. A risk score and risk level are displayed.

---

## Risk Levels

- **Low Risk** – Likely genuine application
- **Medium Risk** – Suspicious indicators detected
- **High Risk** – Strong impersonation or deception signals

Risk scores are heuristic-based and intended to support analysis, not replace official app store moderation.

---

## Setup and Execution

### Install Dependencies

```bash
pip install -r requirements.txt
```
### Run the Application

```bash
python run.py
```
### Access in Browser

http://127.0.0.1:5000

---

## Limitations

- Detection logic is heuristic-based and not ML-trained
- Depends on Play Store search result reliability
- Supports Android applications only

---

## Future Enhancements

- Detailed explanation of detected risk signals
- False-positive tracking and evaluation metrics
- Automated report generation
- Role-based access control (admin vs user)
- Permission and SDK-based risk analysis

---

## Disclaimer

This project is an academic and research prototype.  
It has no official association with Google, NPCI, PhonePe, Paytm, or any other brand.


