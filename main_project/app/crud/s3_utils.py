import boto3
from botocore.exceptions import NoCredentialsError
from app.settings import S3_ACCESS_KEY, S3_SECRET_KEY, S3_BUCKET_NAME, S3_ENDPOINT_URL

# Initialize an S3 client using boto3 with the provided credentials and endpoint configuration.
s3_client = boto3.client('s3', 
                         aws_access_key_id=S3_ACCESS_KEY, 
                         aws_secret_access_key=S3_SECRET_KEY, 
                         endpoint_url=S3_ENDPOINT_URL)

def upload_image_to_s3(image_file, user_id: int):
    """
    Uploads an image file to an S3 bucket and generates a publicly accessible URL.
    """
    try:
        file_name = f"{user_id}_{image_file.filename}"
        s3_client.upload_fileobj(image_file.file, S3_BUCKET_NAME, file_name)
        
        image_url = f"{S3_ENDPOINT_URL}/{S3_BUCKET_NAME}/{file_name}"
        return image_url
    except NoCredentialsError:
        raise Exception("Credentials not available")