#!/usr/bin/env python3
# DB: we'll use psycopg2 for Postgres; in a mock environment imports may not be used,
# so wrap them to provide a helpful error if missing.
try:
import psycopg2
from psycopg2 import sql
except Exception:
psycopg2 = None


# Load environment variables
from dotenv import load_dotenv
load_dotenv()


LOG = logging.getLogger("automation")
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


# Required configuration names (read from environment)
S3_BUCKET = os.getenv("S3_BUCKET_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
EC2_PRIVATE_IP = os.getenv("EC2_PRIVATE_IP")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")


# Helpers
def get_s3_client():
try:
return boto3.client("s3", region_name=AWS_REGION)
except NoCredentialsError:
LOG.error("AWS credentials not found. Please export AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY or configure a profile.")
raise




def upload_log(sample_file: str = "app.log"):
if not S3_BUCKET:
LOG.error("S3_BUCKET_NAME not set in environment")
return False


s3 = get_s3_client()
# Create sample log if not exists
Path(sample_file).write_text("INFO Sample log entry\n")


try:
with open(sample_file, "rb") as f:
s3.put_object(Bucket=S3_BUCKET, Key=sample_file, Body=f)
LOG.info("Uploaded %s to s3://%s/%s", sample_file, S3_BUCKET, sample_file)
return True
except ClientError as e:
LOG.error("Failed to upload file to S3: %s", e)
return False




def list_s3_objects(output_file: str = "s3_objects.txt"):
if not S3_BUCKET:
LOG.error("S3_BUCKET_NAME not set in environment")
return []


s3 = get_s3_client()
try:
paginator = s3.get_paginator("list_objects_v2")
page_iterator = paginator.paginate(Bucket=S3_BUCKET)
objects = []
for page in page_iterator:
for obj in page.get("Contents", []):
objects.append(obj["Key"])


Path(output_file).write_text("\n".join(objects))
LOG.info("Wrote %d object keys to %s", l