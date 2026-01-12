import boto3

def check_public_s3():
    s3 = boto3.client("s3")
    findings = []

    buckets = s3.list_buckets()["Buckets"]

    for bucket in buckets:
        try:
            acl = s3.get_bucket_acl(Bucket=bucket["Name"])
            for grant in acl["Grants"]:
                if "AllUsers" in str(grant):
                    findings.append({
                        "service": "S3",
                        "issue": "Public S3 Bucket",
                        "bucket": bucket["Name"],
                        "severity": "CRITICAL"
                    })
        except Exception:
            continue

    return findings
