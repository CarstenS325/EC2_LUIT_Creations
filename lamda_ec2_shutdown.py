import boto3

s3_client.client('s3')

response = s3.list_buckets()

print(response)