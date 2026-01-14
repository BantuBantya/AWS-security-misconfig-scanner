# AWS Security Misconfiguration Scanner

## Overview
This project is a Python-based security tool designed to identify **high-risk AWS misconfigurations** that commonly lead to real-world cloud breaches.

Instead of focusing on theoretical vulnerabilities, the scanner targets **practical cloud security failures** such as permissive IAM policies, public storage exposure, and open network access.

The project reflects how a **Cloud Security Engineer** proactively detects and prioritizes risk in production AWS environments.

---

## Problem Statement
A significant percentage of cloud breaches occur due to:
- Overly permissive IAM policies
- Publicly accessible S3 buckets
- Misconfigured EC2 security groups

These issues are often overlooked during rapid cloud deployments and later exploited by attackers.

---

## What This Project Does
- Enumerates critical AWS resources using AWS APIs
- Detects common but dangerous security misconfigurations
- Assigns severity-based risk levels
- Generates structured security reports for remediation

---

## Architecture & Workflow

AWS Account

↓

IAM / S3 / EC2 Enumeration

↓

Misconfiguration Detection

↓

Risk Scoring Engine

↓

Security Report (JSON)


---

## Security Checks Implemented

### IAM Policy Analysis
Detects policies with wildcard (`*`) permissions that violate least-privilege principles.

### S3 Bucket Exposure
Identifies publicly accessible S3 buckets that can lead to data leakage.

### EC2 Security Group Analysis
Detects inbound rules allowing unrestricted access (`0.0.0.0/0`).

---

## Risk Scoring
Each finding is categorized by severity:
- **CRITICAL** – Immediate risk with high impact
- **HIGH** – Serious misconfiguration requiring prompt action
- **LOW** – Informational or low-impact findings

This helps prioritize remediation efforts effectively.

---

## Reporting
The tool generates timestamped JSON reports that can be:
- Shared with cloud engineering teams
- Integrated into SOC workflows
- Extended to PDF or HTML formats

---

## Tech Stack
- Python
- AWS (IAM, S3, EC2)
- boto3

---

## Why This Matters
Most cloud incidents are caused by **misconfigurations**, not zero-day exploits.
This project mirrors real detection logic used by cloud security teams.

---

## Disclaimer
Run this tool only on AWS accounts you own or have explicit permission to test.



