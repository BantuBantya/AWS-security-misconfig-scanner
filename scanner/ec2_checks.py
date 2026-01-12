import boto3

def check_open_security_groups():
    ec2 = boto3.client("ec2")
    findings = []

    sgs = ec2.describe_security_groups()["SecurityGroups"]

    for sg in sgs:
        for perm in sg["IpPermissions"]:
            for ip in perm.get("IpRanges", []):
                if ip.get("CidrIp") == "0.0.0.0/0":
                    findings.append({
                        "service": "EC2",
                        "issue": "Open Security Group",
                        "group": sg["GroupName"],
                        "port": perm.get("FromPort"),
                        "severity": "HIGH"
                    })

    return findings
