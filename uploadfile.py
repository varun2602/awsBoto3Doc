import boto3 

# client = boto3.client("s3")
s3 = boto3.client("s3")

fileupload = s3.upload_file('hello.txt', 'example-boto3-12974297', 'hello.txt')
print(fileupload)