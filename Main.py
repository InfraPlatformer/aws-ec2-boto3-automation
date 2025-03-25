import boto3

def launch_ec2():
    with open("config.yml") as f:
        config = yaml.safe_load(f)
    
    ec2 = boto3.client('ec2', region_name=config['region'])
    
    for instance in config['instances']:
        response = ec2.run_instances(
            ImageId=instance['ami'],
            InstanceType=instance['type'],
            KeyName=instance['key_pair'],
            SecurityGroups=instance['security_groups'],
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': instance['name']}]
            }]
        )
        print(f"Launched {instance['name']}: {response['Instances'][0]['InstanceId']")

if __name__ == "__main__":
    launch_ec2()
