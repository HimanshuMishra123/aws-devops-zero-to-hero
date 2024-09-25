import boto3                                      # To import boto3 package

def lambda_handler(event, context):               # It receives event and context parameters from AWS when the function is invoked
    ec2 = boto3.client('ec2')                     # create a client name EC2 to to interact with ec2 service

    # Get all EBS snapshots
    response = ec2.describe_snapshots(OwnerIds=['self'])

    # The describe_instances method is called with a filter to get only the EC2 instances that are currently running.
    # filtter use krte hai specific tarah ke instance filtter out krne ke liye
    instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
   

    #Create a Set of Active Instance IDs ,by iterating through the list of running instances and adds their Instance IDs to this set.
    active_instance_ids = set()                   #creating a empty set to store EC2 ids
    for reservation in instances_response['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])

    # Iterate through each snapshot and delete if it's not attached to any volume or the volume is not attached to a running instance
    for snapshot in response['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')        # .get is used as it so happen that volume id is not present then earlier method will give key error but .get return "None"    

        if not volume_id:
            # Delete the snapshot if it's not attached to any volume
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted EBS snapshot {snapshot_id} as it was not attached to any volume.")
        else:
            # Check if the volume still exists
            try:
                volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
                if not volume_response['Volumes'][0]['Attachments']:  # deleting snapshot if volume is not attached to any EC2 instance
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.")
           
            except ec2.exceptions.ClientError as e:        # The volume associated with the snapshot itself is not found (it might have been deleted), which will through an error
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':  
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")
