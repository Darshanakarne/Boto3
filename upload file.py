import boto3
client = boto3.client('s3')

file_reader = open('create_bucket.py').read()
response = client.put_object(
    ACL='private',
    Body=file_reader,
    Bucket='11april22darshana',
    Key='create_bucket.py'
)