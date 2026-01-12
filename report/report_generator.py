import json
from datetime import datetime

def generate_report(findings, output_format="json"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"aws_security_report_{timestamp}"

    if output_format == "json":
        with open(f"{filename}.json", "w") as f:
            json.dump(findings, f, indent=4)

        print(f"[+] Report generated: {filename}.json")

    elif output_format == "txt":
        with open(f"{filename}.txt", "w") as f:
            f.write("AWS Security Misconfiguration Report\n")
            f.write("=" * 40 + "\n\n")

            for item in findings:
                for k, v in item.items():
                    f.write(f"{k}: {v}\n")
                f.write("-" * 30 + "\n")

        print(f"[+] Report generated: {filename}.txt")
