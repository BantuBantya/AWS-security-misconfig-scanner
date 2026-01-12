from scanner.iam_checks import check_iam_policies
from scanner.s3_checks import check_public_s3
from scanner.ec2_checks import check_open_security_groups
from scanner.risk_engine import calculate_risk
from report.report_generator import generate_report

def main():
    print("\n[+] Starting AWS Security Misconfiguration Scan...\n")

    findings = []
    findings += check_iam_policies()
    findings += check_public_s3()
    findings += check_open_security_groups()

    calculate_risk(findings)
    generate_report(findings, output_format="json")

if __name__ == "__main__":
    main()
