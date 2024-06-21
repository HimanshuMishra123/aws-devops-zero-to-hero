import boto3
import json

#lambda_handler function is triggered by aws config
#event parameter contains data(JSON) that triggered the labda function (Example - if your function is triggered by a change in an EC2 instance configuration, event will include information about that change)
#context parameter contains information about the Lambda function’s execution environment. Example - Request ID , Function name etc.
def lambda_handler(event, context):          

    # Get the specific EC2 instance.
    ec2_client = boto3.client('ec2')
    

    # Assume compliant by default
    compliance_status = "COMPLIANT"  
    

    #example of "event" data  ....
    #event = {
    #"invokingEvent": "{\"configurationItem\": {\"configuration\": {\"instanceId\": \"i-0123456789abcdef0\"}}, \"notificationCreationTime\": \"2024-06-21T12:00:00Z\"}",
    #"resultToken": "example-token"
    # }
    # Extract the invoking event item from the event data and parsing the Json to dict.
    config = json.loads(event['invokingEvent'])   
    # Extract the configuration item 
    configuration_item = config["configurationItem"]
    # Extract the instanceId
    instance_id = configuration_item['configuration']['instanceId']
    

    # Get complete Instance details
    instance = ec2_client.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]
    
    # Check if the specific EC2 instance has Cloud Trail logging enabled.
    
    if not instance['Monitoring']['State'] == "enabled":
        compliance_status = "NON_COMPLIANT"

    evaluation = {
        'ComplianceResourceType': 'AWS::EC2::Instance',
        'ComplianceResourceId': instance_id,
        'ComplianceType': compliance_status,
        'Annotation': 'Detailed monitoring is not enabled.',
        'OrderingTimestamp': config['notificationCreationTime']
    }
    
    config_client = boto3.client('config')              # in boto3 config doc search "put_evaluations"
    
    response = config_client.put_evaluations(
        Evaluations=[evaluation],
        ResultToken=event['resultToken']    #Identifies the rule and the event that triggered the evaluation.


    )  
    
    return response
