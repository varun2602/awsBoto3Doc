import boto3 

client = boto3.client("s3")

response = client.create_bucket(
   
    Bucket='example-boto3-12974297',
    CreateBucketConfiguration={
        'LocationConstraint':'us-east-2'
    })

print(response)