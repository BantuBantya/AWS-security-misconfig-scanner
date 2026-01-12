import boto3

def check_iam_policies():
    iam = boto3.client("iam")
    findings = []

    policies = iam.list_policies(Scope='Local')['Policies']

    for policy in policies:
        policy_version = iam.get_policy_version(
            PolicyArn=policy['Arn'],
            VersionId=policy['DefaultVersionId']
        )

        statements = policy_version['PolicyVersion']['Document']['Statement']

        for stmt in statements:
            if stmt.get("Effect") == "Allow" and stmt.get("Resource") == "*":
                findings.append({
                    "service": "IAM",
                    "issue": "Over-Permissive Policy",
                    "policy": policy['PolicyName'],
                    "severity": "HIGH"
                })

    return findings
