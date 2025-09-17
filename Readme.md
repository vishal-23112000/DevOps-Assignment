# DevOps Assignment

This repository demonstrates a **mock DevOps workflow**, including Infrastructure as Code (Terraform), automation scripts (Python), and a CI/CD pipeline (GitHub Actions).

---

## Project Structure

├── terraform/ # Terraform modules and definitions
│ ├── modules/ # Reusable Terraform modules (S3, RDS, EC2)
│ ├── main.tf # Terraform root configuration
│ ├── variables.tf
│ ├── outputs.tf
│ └── terraform.tfvars.example
├── scripts/ # Automation scripts (Python)
│ └── automation.py
├── .github/
│ └── workflows/
│ └── main.yml # GitHub Actions CI/CD pipeline
├── .env.example # Environment variables template
├── requirements.txt # Python dependencies
└── README.md

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/DevOps-Assignment.git
cd DevOps-Assignment

Install Python dependencies
pip install -r requirements.txt

Configure environment variables
cp .env.example .env
# Update .env with actual AWS credentials, RDS endpoint, S3 bucket, and EC2 private IP


Run the automation script
python scripts/automation.py


Verify outputs

app.log uploaded to S3 bucket

logs table created in RDS, with a sample row inserted and printed

EC2 metadata printed in JSON

s3_objects.txt contains the list of objects in S3
