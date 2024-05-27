import json
import boto3
import botocore
import time   



def lambda_handler(event, context):
    
    ec2_client = boto3.client("ec2")
    elb_client = boto3.client('elb')
    
    vpc = ec2_client.create_vpc(
        CidrBlock = "",  
            )
            
    time.sleep(3)
    
    ec2_client.create_tags(
    Resources=[vpc['Vpc']['VpcId'],],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'VPC for Testing'
                },
            ]   
        )     
            
    subnet_1=ec2_client.create_subnet(
        CidrBlock = '',
        AvailabilityZone="ap-south-1a",
        VpcId= vpc['Vpc']['VpcId'],        
        )  
        
    time.sleep(3)
    
    ec2_client.create_tags(
    Resources=[subnet_1['Subnet']['SubnetId'],],
    Tags=[
        {
            'Key': 'Name',    
            'Value': 'Subnet1 for Testing'
                },
            ]   
        ) 
    
                
    subnet_2=ec2_client.create_subnet(
        AvailabilityZone="ap-south-1b",
        VpcId= vpc['Vpc']['VpcId'],     
        CidrBlock = ''
        )
        
    time.sleep(3)    
        
    ec2_client.create_tags(
    Resources=[subnet_2['Subnet']['SubnetId'], ],      
    Tags=[
        {
            'Key': 'Name',
            'Value': 'Subnet2 for Testing'    
                },
            ]   
        ) 
    
        
    
    print(subnet_2)
    print(vpc)   
    
