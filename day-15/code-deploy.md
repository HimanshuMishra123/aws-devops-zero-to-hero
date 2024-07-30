To deploy a project using AWS CodeDeploy, you can follow these steps. This guide assumes you have an AWS account, necessary permissions, and a UI project ready for deployment. AWS CodeDeploy can be used to deploy applications to Amazon EC2 instances, on-premises instances, or AWS Lambda functions. Here, we'll focus on deploying to EC2 instances.


### AWS CodeDeploy
AWS CodeDeploy is a fully managed deployment service that automates software deployments to various compute services such as Amazon EC2, AWS Fargate, and on-premises servers. The **CodeDeploy agent** is software installed on the instances or servers where applications will be deployed. It communicates with the CodeDeploy service to fetch the application files, validate them, and then deploy them according to the specified deployment configuration.


### Step 1: Prepare the Application Specification File (AppSpec.yml)

The `appspec.yml` file defines how to deploy the application. This file should be included in the root of your source code.

Example `appspec.yml` for a simple UI project:

```yaml
version: 0.0
os: linux
files:
  - source: /path/to/source
    destination: /var/www/html
hooks:
  BeforeInstall:
    - location: scripts/install_dependencies.sh
      timeout: 300
      runas: root
  AfterInstall:
    - location: scripts/start_server.sh
      timeout: 300
      runas: root
```

- **files**: Defines the source and destination paths for the deployment.
- **hooks**: Defines lifecycle event hooks to run scripts at various stages of the deployment.

### Step 2: Set Up the Deployment Environment

1. **EC2 Instances**:
   - Ensure you have EC2 instances set up with the necessary environment to run your application.(in EC2>> tags>> key: specific key(ex-project), Value: <name-of-your-app/project>)
   - The ec2 instances should have the `CodeDeploy agent` installed and running where app is to be deployed. You can install the agent using a script from the AWS documentation or include it in your instance setup script. To Install the CodeDeploy agent for Ubuntu Server use document link...  https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install-ubuntu.html
    - while using the document when on 4th point(wget command), check  `Resource kit bucket names by Region` by clicking on it to get the bucket name as per the region 
    - systemctl commands to be run with sudo.
    - whenever you do any configurations always restart the  `CodeDeploy agent`>> sudo service codedeploy-agent restart

2. **IAM Roles**:
   - Create an IAM role for CodeDeploy with the necessary permissions to deploy your application to the target instances.
   - Ensure the EC2 instances also have a role that allows them to interact with CodeDeploy (e.g., `AmazonEC2RoleforAWSCodeDeploy` policy).
- whenever you do any configurations always restart the  `CodeDeploy agent`>> sudo service codedeploy-agent restart

### Step 3: Create/setup a Deployment Group in CodeDeploy service

1. **Navigate to AWS CodeDeploy**:
   - In the AWS Management Console, go to CodeDeploy under the "Developer Tools" section.

2. **Create a New Application**:
   - Click "Create application."
   - **Application Name**: Enter a name for your application.
   - **Compute Platform**: Choose "EC2/On-premises" for deploying to EC2 instances.(from options of EC2/on-premise, AWS Lambda, Amazon ECS)  >>> click on create application

3. **Create a Deployment Group**:
   - **Deployment Group Name**: Enter a name for the deployment group.(example- microservice name or service to which the ec2 instance belongs )
   - **Service Role**: Select the IAM role that allows CodeDeploy to deploy to your instances.
   - **Deployment Type**: Choose between "In-place" (updates the same instances) or "Blue/Green" (deploys to a new set of instances).
   - **Environment Configuration**: Define the instances to which CodeDeploy will deploy the application. This can be done using tags, Auto Scaling groups, or manually selected instances.(example: if EC2 instance the in tags>> key: specific key(ex-project), Value: <name-of-your-app/project>). If the same tag is on 10 EC2 instance then it can deploy app to group of 10 EC2 instance.
   - **Deployment Settings**:`(you can ignore this step for now, only needed in org. setup)` >> Configure additional settings like deployment configurations (e.g., OneAtATime, HalfAtATime), rollback behavior, and monitoring options.
   - **Load Balancer**: Disable/deselect it. as we don't need load balancer for deployment
    
     >> click on `create deployment group`

### Step 4: Deploy the Application

1. **Prepare the Application Bundle**:
   - Package your application files, including the `appspec.yml` file and any necessary scripts. This can be done using a ZIP file or other supported formats.
   - `appspec.yml` file defines how to deploy an application. It contains deployment instructions, including where application files should be copied, what scripts should be run before and after the deployment, and other deployment lifecycle events. `appspec.yml` should be at the root of your repo.


```yaml
version: 0.0
os: linux
files:
  - source: /path/to/source
    destination: /var/www/html
hooks:
  BeforeInstall:
    - location: scripts/install_dependencies.sh
      timeout: 300
      runas: root
  AfterInstall:
    - location: scripts/start_server.sh
      timeout: 300
      runas: root
```
>> write separate shell file start_server.sh and install_dependencies.sh 

2. **Upload the Application Bundle to you code versioning area**:
   - Upload the package to an S3 bucket or an external repository(on github) if not using CodeCommit.

3. **Create a Deployment**:
   - Go to your CodeDeploy application and under deployment click on "Create deployment."
   - **Deployment Group**: Select the deployment group created earlier.
   - **Revision Type**: Select where your application bundle is stored (e.g., S3, GitHub).
   - **Revision Location**: Provide the path/repo name(HimanshuMishra123/aws-devops-zero-to-hero) to your application bundle.>> if you are doing complete CI/CD then `commit id` is not needed but if you just want to test the CD then provide latest commit id of that repo.
>> click on `create deployment`

4. **Start the Deployment**:
   - Start the deployment and monitor its progress in the CodeDeploy console. The console will display the status and any logs from the deployment lifecycle events.

### Step 5: Verify the Deployment

1. **Check the Application**:
   - Verify that the application is deployed correctly by accessing the EC2 instance or the web server where it’s hosted.

2. **Monitor Logs and Metrics**:
   - Use CloudWatch Logs, CodeDeploy logs, and CloudWatch metrics to monitor the application's performance and health.

3. **Rollback if Necessary**:
   - If the deployment encounters issues, use the rollback options configured in the deployment group settings.

By following these steps, you can set up and use AWS CodeDeploy to automate the deployment of a UI project to EC2 instances, ensuring a consistent and reliable deployment process.