import boto3
from botocore.config import Config
from botocore.exceptions import ClientError

def upload(file,final_path):
    """upload file to aws"""
    s3_client = boto3.client(
        's3',
        aws_access_key_id= 'S3RVER',
        aws_secret_access_key= 'S3RVER',
        endpoint_url = 'http://localhost:4569'
        # aws_access_key_id= 'AKIAZYHH7OISLSKW7ORM',
        # aws_secret_access_key= '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'
    )
    try:
        print(s3_client.put_object(
            Body = file,
            Bucket = 'local-bucket',
            # Bucket = 'anibal-test-pdf',
            Key = final_path,
        ))
        return True
    except Exception as e:
        print(e)
        return False