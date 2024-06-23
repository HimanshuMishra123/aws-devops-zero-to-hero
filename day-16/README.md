# AWS CLOUD WATCH 

**Introduction to AWS CloudWatch:**
- CloudWatch is a monitoring and management service provided by AWS.
- It can be described as a "gatekeeper" or "watchman" for AWS resources, continuously observing and reporting on activities within the AWS environment.
- It monitors various AWS resources like EC2 instances, S3 buckets, RDS instances, and more, and provides insights through metrics, logs, and sets alarms to alert you on certain conditions.

**Key Features of CloudWatch:**

1. **Monitoring:**
   - Fundamental feature used to observe the health and performance of AWS resources.
   - Includes infrastructure monitoring (EC2 instances, RDS, Lambda functions etc.) and application monitoring.

2. **Metrics (real-life metrics):**
   - Metrics are quantitative measurements that CloudWatch collects from AWS resources.
   - Examples include CPU utilization, memory usage, and API request counts.
   - Metrics provide detailed insights into resource usage and performance.

3. **Alarms:**
   - Alarms are set on metrics to take automated actions when thresholds are crossed.
   - Example: An alarm can be configured to send an email notification if an EC2 instance’s CPU utilization exceeds 80%.

4. **Logs:**
   - CloudWatch Logs(log groups) collect and monitor log files from AWS resources and applications by default and you can also create log groups
   - Provides detailed insights into system events and application behaviors.
   - log insights: Provides advanced Sql like query capabilities on log data, helping to analyze, troubleshoot, and optimize applications.(you can save frequently used queries, share, check the history of queries to re-run them)
   - Live Tail: Real-time view of log data as it is being ingested. Useful for debugging and monitoring applications during deployment.
   - Log Anomalies:  Automatically detects unusual patterns in log data. Helps in identifying and troubleshooting issues without predefined thresholds.
     Contributor Insights: Analyze log data and create a time series that displays contributor data. You can see metrics about the top-N contributors, the total number of unique contributors, and their usage. This helps you find top talkers and understand who or what is impacting system performance.

5. **Custom Metrics:**
   - Allows users to create their own metrics to monitor aspects not covered by default metrics.
   - Example: Monitoring memory usage on an EC2 instance which is not available as a default metric.

6. **Cost Optimization:**
   - By analyzing resource usage and performance, CloudWatch helps in identifying underutilized resources, aiding in cost reduction.
   - Can be integrated with AWS Lambda to automate cost-saving measures.
   - For example-  deleting snapshots that are not associated with any volume-id and volume-id is not attached to running EC2.

7. **Scaling:**
   - Helps in scaling resources by providing data that can trigger actions in other AWS services like Auto Scaling.
   - Example: Automatically adding new EC2 instances when CPU utilization is high or reaches to certain level.

CloudWatch helps address several critical challenges/problems, including:

    Resource Utilization: Tracking resource utilization and performance metrics to optimize your AWS infrastructure efficiently.
    Proactive Monitoring: Identifying and resolving issues before they impact your applications or users.
    Troubleshooting: Analyzing logs and metrics to troubleshoot problems and reduce downtime.
    Scalability: Automatically scaling resources based on demand to ensure optimal performance and cost efficiency.

Practical Use Cases of AWS CloudWatch:

    Auto Scaling: CloudWatch can trigger Auto Scaling actions based on defined thresholds. For example, you can automatically scale in or out based on CPU utilization or request counts.

    Resource Monitoring: Monitor EC2 instances, RDS databases, DynamoDB tables, and other AWS resources to gain insights into their performance and health.

    Application Insights: Track application-specific metrics to monitor the performance of your applications and identify potential bottlenecks.

    Log Analysis: Use CloudWatch Logs Insights to analyze log data, identify patterns, and troubleshoot issues in real-time.

    Billing and Cost Monitoring: CloudWatch can help you monitor your AWS billing and usage patterns, enabling you to optimize costs.


**Concepts Explained:**

- **Metric:**
  - A metric is a time-ordered set of data points.
  - Example metrics: CPU utilization, memory consumption, API request count.

- **Alarm:**
  - Alarms are configured to monitor metrics and perform actions based on metric data.
  - Actions can include sending notifications or triggering auto-scaling.

- **Logs:**
  - Logs capture detailed records of events that occur in your AWS environment.
  - Example: Access logs for an S3 bucket or error logs for an EC2 instance.

- **Custom Metrics:**
  - Custom metrics are user-defined metrics to track specific data points not available by default.
  - Example: Memory usage of an application running on an EC2 instance.
