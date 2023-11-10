import boto3
from botocore.exceptions import NoCredentialsError


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3')

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print(f"Upload Successful. {s3_file} has been uploaded to {bucket}")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


def download_from_aws(bucket, s3_file, local_file):
    s3 = boto3.client('s3')

    try:
        s3.download_file(bucket, s3_file, local_file)
        print(f"Download Successful. {s3_file} has been downloaded from {bucket}")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


local_file_name = 'work.jpg'
bucket_name = 'norkos'
s3_file_name = 'file_in_s3.jpg'

upload_to_aws(local_file_name, bucket_name, s3_file_name)
download_from_aws(bucket_name, s3_file_name, f"fetched_{local_file_name}")
