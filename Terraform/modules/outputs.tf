output "s3_bucket_id" {
value = module.s3_logs.bucket_id
}


output "rds_endpoint" {
value = module.rds_db.endpoint
}


output "ec2_private_ip" {
value = module.ec2_app.private_ip
}