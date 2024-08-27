import boto3

cloudfront = boto3.client('clouldfront')

distributionlist = response['Vpcs']

vpcs - response['Vcps']

for vpc in vcps: 
    print(vpc['VpcId'])