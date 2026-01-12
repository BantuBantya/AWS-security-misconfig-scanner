from colorama import Fore, Style

def calculate_risk(findings):
    score = 0

    print("\n[+] Scan Results:\n")

    for f in findings:
        sev = f["severity"]
        if sev == "CRITICAL":
            score += 10
            color = Fore.RED
        elif sev == "HIGH":
            score += 6
            color = Fore.YELLOW
        else:
            score += 2
            color = Fore.GREEN

        print(color + str(f) + Style.RESET_ALL)

    print(f"\n[!] Overall Risk Score: {score}")
