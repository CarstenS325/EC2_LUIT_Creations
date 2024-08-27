import boto3

cloudfront = boto2.client('clouldfront')

distributionlist = response['Vpcs']

vpcs - response['Vcps']

for vpc in vcps: 
    print(vpc['VpcId'])