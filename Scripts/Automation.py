#!/usr/bin/env python3
import os
import json
import logging
import boto3
import psycopg2
from botocore.exceptions import ClientError
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
EC2_PRIVATE_IP = os.getenv("EC2_PRIVATE_IP")

# AWS clients
s3_client = boto3.client("s3", region_name=AWS_REGION)
ec2_client = boto3.client("ec2", region_name=AWS_REGION)

def upload_log_to_s3():
    log_file = "app.log"
    try:
        with open(log_file, "w") as f:
            f.write("Sample log entry for DevOps assignment\n")
        s3_client.upload_file(log_file, S3_BUCKET_NAME, log_file)
        logger.info(f"Uploaded {log_file} to S3 bucket {S3_BUCKET_NAME}")
    except ClientError as e:
        logger.error(f"Failed to upload log: {e}")

def rds_operations():
    try:
        conn = psycopg2.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASSWORD, dbname=DB_NAME, connect_timeout=5
        )
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id SERIAL PRIMARY KEY,
                message TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        cur.execute("INSERT INTO logs (message) VALUES (%s)", ("Hello from DevOps assignment",))
        conn.commit()
        cur.execute("SELECT * FROM logs;")
        rows = cur.fetchall()
        logger.info("Logs table content:")
        for row in rows:
            logger.info(row)
        cur.close()
        conn.close()
    except Exception as e:
        logger.error(f"RDS operation failed: {e}")

def get_ec2_metadata():
    try:
        response = ec2_client.describe_instances(
            Filters=[{"Name": "private-ip-address", "Values": [EC2_PRIVATE_IP]}]
        )
        reservations = response.get("Reservations", [])
        if not reservations:
            logger.warning("No EC2 instance found for the given private IP.")
            return
        instance = reservations[0]["Instances"][0]
        metadata = {
            "InstanceId": instance["InstanceId"],
            "InstanceType": instance["InstanceType"],
            "Region": AWS_REGION,
            "PrivateIp": instance["PrivateIpAddress"]
        }
        print(json.dumps(metadata, indent=2))
    except ClientError as e:
        logger.error(f"Error retrieving EC2 metadata: {e}")

def list_s3_objects():
    try:
        response = s3_client.list_objects_v2(Bucket=S3_BUCKET_NAME)
        objects = [obj["Key"] for obj in response.get("Contents", [])] if "Contents" in response else []
        with open("s3_objects.txt", "w") as f:
            for obj in objects:
                f.write(obj + "\n")
        logger.info(f"Listed {len(objects)} objects in S3 bucket {S3_BUCKET_NAME}")
    except ClientError as e:
        logger.error(f"Failed to list objects: {e}")

if __name__ == "__main__":
    upload_log_to_s3()
    rds_operations()
    get_ec2_metadata()
    list_s3_objects()
