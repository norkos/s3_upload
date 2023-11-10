import boto3
from names_generator import generate_name
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


def create_folder_in_s3(bucket, folder_name):
    s3 = boto3.client('s3')

    folder_key = folder_name + '/'
    try:
        s3.put_object(Bucket=bucket, Key=folder_key)
        print(f"Folder '{folder_name}' created in bucket '{bucket}'")
    except NoCredentialsError:
        print("Credentials not available")


dir_name = generate_name()
file_name = 'work.jpg'
bucket_name = 'norkos'
s3_file_name = f"{dir_name}/{file_name}"

create_folder_in_s3(bucket_name, dir_name)
upload_to_aws(file_name, bucket_name, s3_file_name)
download_from_aws(bucket_name, s3_file_name, f"fetched_{file_name}")
