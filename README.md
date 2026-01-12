\# AWS Security Misconfiguration Scanner



\## Problem

Cloud breaches often occur due to misconfigured IAM policies, public storage, and open network access.



\## Solution

This tool scans an AWS account for high-risk security misconfigurations and assigns a risk score.



\## Checks Implemented

\- Over-permissive IAM policies

\- Publicly accessible S3 buckets

\- Open EC2 security groups (0.0.0.0/0)



\## Tech Stack

\- Python

\- AWS (IAM, S3, EC2)

\- boto3



\## Why This Matters

These misconfigurations directly map to real-world cloud breaches.



\## Future Enhancements

\- Terraform integration

\- Auto-remediation

\- CIS Benchmark mapping



