# AWS Config

Note: In every organizational projects(Banking, financial, government) there are compliance and security poilicies/rules which we have to follow and implement. As a DevOps Engineer we have to ensure that all the resources in the AWS account are basically compliant to organizational rules and regulations.  <br/>

![Day-25 _ AWS Config _ Identify Compliant and Non Compliant AWS resources   _#aws #abhishekveeramalla 18-25 screenshot](https://github.com/HimanshuMishra123/aws-devops-zero-to-hero/assets/164254902/42a678df-9af4-4972-9dc3-97c45ad0de45)


Note: you might be thinking how will I come to know about these things, you have to ask you manager that I want to set up the compliance rules and I want to set up AWS config and I want to verify how many resources are compliant and how many resources are non-compliant and I want to give you a detailed information can you provide me detailed set of rules and regulations that you are looking for right, so this is what you do using AWS config now this is very very important because complaints is related to security Whenever there is something related to security your organization takes that as the highest priority.<br/>

one such example that I've taken is this one that is ec2 detailed monitoring.<br/>

we'll use AWS Config to detect compliant and non-compliant ec2 instances for below rule.
- compliant ec2 instance has monitoring enabled
- non-compliant ec2 instance does not have monitoring enabled

Step 1: Set Up AWS Config

    Log in to your AWS Management Console.

    Navigate to the AWS Config service.

    Click on "Get started" if you're using AWS Config for the first time.

    Configure the delivery channel settings, which include specifying an Amazon S3 bucket where AWS Config will store configuration history.

    Choose the resource types you want AWS Config to monitor. In this case, select "Amazon EC2 Instances."
![image](https://github.com/HimanshuMishra123/aws-devops-zero-to-hero/assets/164254902/7e83e374-483c-4f4b-8822-5628b92065bf)
![image](https://github.com/HimanshuMishra123/aws-devops-zero-to-hero/assets/164254902/a718126b-fc89-4fec-91a3-c1ae5d910988)


Step 2: Create a Custom Config Rule

    Navigate to the AWS Config console.

    In the left navigation pane, click on "Rules."

    Click on the "Add rule" button.

    Choose "Create a custom rule."

    Give your rule a name and description (e.g., "Monitoring for EC2 Instances").

    For "Scope of changes," choose "Resources."

    Define the rule trigger. You can use AWS Lambda as the trigger source. If you haven't already created a Lambda function for this rule, create one that checks whether monitoring is enabled for an EC2 instance. The Lambda function will return whether the resource is compliant or not based on monitoring status.

Step 3: Define the Custom Rule in AWS Config

    Choose your Lambda function from the dropdown list as the evaluator for the rule.

    Specify the trigger type (e.g., "Configuration changes").

    Save the rule.

Step 4: Monitor and Alert

    AWS Config will now continuously watch your EC2 instances and evaluate against the rule you've created.

    If any EC2 instance is found without monitoring enabled, the custom rule's Lambda function will mark it as non-compliant.
