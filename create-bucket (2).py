import boto3
client = boto3.client('s3')

response = client.create_bucket(
    ACL='private',
    Bucket='11april22darshana',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-northeast-1'
    }
)

