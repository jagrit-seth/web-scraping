import boto3
import extract_media_urls
import upload_to_S3
import os
from dotenv import load_dotenv
from logger import configure_logger

load_dotenv()

aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_DEFAULT_REGION")

logger = configure_logger("web_scraping.log")

def main():
    media_urls = extract_media_urls.extract_media_urls()
    if media_urls:
        s3 = boto3.client('s3',
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  region_name=aws_region)
        s3_bucket = 'test-web-scraping'
        upload_to_S3.upload_to_S3(s3, media_urls, s3_bucket)

if __name__ == "__main__":
    main()
