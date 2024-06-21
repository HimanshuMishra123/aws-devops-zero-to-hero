# Comparison of AWS Config, CloudTrail, and CloudWatch :

### AWS Config
- **Purpose:** Tracks and records the configuration of AWS resources.
- **Use:** Monitors changes to resource settings and ensures they comply with your rules.
- **Example:** Checks if your S3 buckets have encryption enabled and alerts you if they don’t.

### AWS CloudTrail
- **Purpose:** Logs all API calls and user actions in your AWS account.
- **Use:** Audits who did what and when in your AWS environment.
- **Example:** Tracks if someone modifies an IAM policy or deletes an EC2 instance.

### Amazon CloudWatch
- **Purpose:** Monitors the performance and operational health of AWS resources.
- **Use:** Collects metrics, logs, and sets alarms for resource health and performance.
- **Example:** Sends an alert if your CPU usage on an EC2 instance is too high.

### Summary
- **AWS Config:** Configuration tracking and compliance monitoring.
- **AWS CloudTrail:** User activity and API call logging.
- **Amazon CloudWatch:** Performance monitoring and operational health.