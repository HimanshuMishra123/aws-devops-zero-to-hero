**Custom Metrics Example on setting up custom metrics for EC2 instance memory utilization using AWS CloudWatch Agent:**


### Overview

To monitor EC2 instance memory utilization, you can use the AWS CloudWatch Agent to send custom metrics to CloudWatch. By default, EC2 instances do not report memory utilization to CloudWatch, so you need to configure the CloudWatch Agent to collect and push these metrics. CloudWatch Agent automatically collects and sends metrics like memory utilization, disk space, and more to Cloudwatch without needing manual intervention or scripting.

### Steps to Set Up CloudWatch Agent on EC2 for Custom Metrics

#### 1. **Install CloudWatch Agent**

1. **Connect to your EC2 instance:**
   - SSH into your EC2 instance using your preferred method.

2. **Download and Install the CloudWatch Agent:**
   - For Amazon Linux 2 or Ubuntu:
     ```bash
     sudo yum install amazon-cloudwatch-agent
     # or
     sudo apt-get install amazon-cloudwatch-agent
     ```
   - For other Linux distributions, download the package from the [AWS CloudWatch Agent download page](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-commandline.html).

#### 2. **Create a CloudWatch Agent Configuration File**

1. **Create the Configuration File:**
   - Use the configuration wizard to create a `config.json` file. Run the following command:
     ```bash
     sudo amazon-cloudwatch-agent-config-wizard
     ```
   - Answer the prompts based on your requirements (choose to collect memory metrics).

2. **Review/Edit Configuration File:**
   - The wizard creates a configuration file at `/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json`. Verify that the configuration includes memory metrics. The section should look like this:
     ```json
     "metrics": {
         "metrics_collected": {
             "mem": {
                 "measurement": [
                     "mem_used_percent"
                 ],
                 "metrics_collection_interval": 60
             }
         }
     }
     ```

#### 3. **Start the CloudWatch Agent**

1. **Start the Agent with the Configuration File:**
   - Run the following command to start the CloudWatch Agent:
     ```bash
     sudo amazon-cloudwatch-agent-ctl -a start -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
     ```

2. **Verify the Agent Status:**
   - Ensure the CloudWatch Agent is running correctly:
     ```bash
     sudo systemctl status amazon-cloudwatch-agent
     ```

#### 4. **Verify Custom Metrics in CloudWatch**

1. **Open the CloudWatch Console:**
   - Go to the CloudWatch console in the AWS Management Console.

2. **Navigate to Metrics:**
   - Select the “Metrics” section from the left-hand menu.

3. **Select the EC2 Namespace:**
   - Choose the “CWAgent” namespace to view the custom metrics collected by the CloudWatch Agent.

4. **Find Memory Metrics:**
   - Look for metrics related to memory utilization (e.g., `mem_used_percent`).

### Conclusion

By following these steps, you will have set up custom metrics for monitoring EC2 instance memory utilization using the AWS CloudWatch Agent. These metrics will now be available in CloudWatch for visualization and alerting.

---
---


### Setting Up CloudWatch Agent in EKS

you can use the CloudWatch Agent in Amazon EKS (Elastic Kubernetes Service) to monitor applications. However, the setup is slightly different from monitoring EC2 instances. Here’s a guide on how to set up the CloudWatch Agent in an EKS cluster:

#### 1. **Create a CloudWatch Agent Configuration File**

1. **Prepare Configuration File:**
   - You need a configuration file for the CloudWatch Agent in JSON format. This file specifies what metrics to collect. For example:
     ```json
     {
       "metrics": {
         "metrics_collected": {
           "statsd": {
             "metrics_collection_interval": 60,
             "service_address": ":8125"
           }
         }
       }
     }
     ```

2. **Store Configuration in a ConfigMap:**
   - Create a ConfigMap in Kubernetes to store the CloudWatch Agent configuration file.
     ```yaml
     apiVersion: v1
     kind: ConfigMap
     metadata:
       name: cwagent-config
       namespace: kube-system
     data:
       cwagent-config.json: |
         {
           "metrics": {
             "metrics_collected": {
               "statsd": {
                 "metrics_collection_interval": 60,
                 "service_address": ":8125"
               }
             }
           }
         }
     ```

#### 2. **Deploy the CloudWatch Agent as a DaemonSet**

1. **Create a DaemonSet YAML File:**
   - Define a DaemonSet to ensure the CloudWatch Agent runs on all nodes in the EKS cluster.
     ```yaml
     apiVersion: apps/v1
     kind: DaemonSet
     metadata:
       name: cloudwatch-agent
       namespace: kube-system
     spec:
       selector:
         matchLabels:
           name: cloudwatch-agent
       template:
         metadata:
           labels:
             name: cloudwatch-agent
         spec:
           containers:
           - name: cloudwatch-agent
             image: amazon/cloudwatch-agent:latest
             volumeMounts:
             - name: cwagent-config
               mountPath: /etc/cwagentconfig
               readOnly: true
             ports:
             - name: statsd
               containerPort: 8125
           volumes:
           - name: cwagent-config
             configMap:
               name: cwagent-config
     ```

2. **Apply the DaemonSet:**
   - Deploy the CloudWatch Agent DaemonSet to your EKS cluster.
     ```bash
     kubectl apply -f cloudwatch-agent-daemonset.yaml
     ```

#### 3. **Configure IAM Roles and Policies**

1. **Create an IAM Role:**
   - Ensure the IAM role attached to your EKS worker nodes has the necessary permissions for CloudWatch.
   - Attach policies like `CloudWatchAgentServerPolicy` to the IAM role.

2. **Associate IAM Role with Nodes:**
   - Ensure that the IAM role is associated with the nodes or the EKS cluster.

#### 4. **Verify Metrics in CloudWatch**

1. **Open the CloudWatch Console:**
   - Go to the CloudWatch console in the AWS Management Console.

2. **Navigate to Metrics:**
   - Check the “CWAgent” namespace to view the metrics collected by the CloudWatch Agent.

3. **Create Dashboards/Alarms:**
   - Use CloudWatch dashboards and alarms to visualize and monitor your metrics.

### Conclusion

Deploying the CloudWatch Agent as a DaemonSet in EKS allows you to collect and monitor both system and application metrics from your Kubernetes nodes. This setup provides centralized monitoring and can be integrated with CloudWatch's visualization and alerting features.

