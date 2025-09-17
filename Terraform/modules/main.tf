module "s3_logs" {
source = "./modules/s3"


bucket_name = "devops-assignment-logs-example"
acl = "private"
versioning = true
tags = var.common_tags
}


module "rds_db" {
source = "./modules/rds"


name = "devops-rds"
identifier = "devops-rds-instance"
engine = "postgres"
engine_version = "15"
family = "postgres15"
instance_class = "db.t3.micro"
allocated_storage = 20
username = "dbadmin"
password = "change_me_password"
db_name = "appdb"
subnet_ids = var.private_subnet_ids
vpc_security_group_ids = var.vpc_security_group_ids
tags = var.common_tags
}


module "ec2_app" {
source = "./modules/ec2"


name = "devops-ec2"
ami = "ami-0abcdef1234567890" # example Amazon Linux AMI (mock)
instance_type = "t3.micro"
subnet_id = var.public_subnet_id
vpc_security_group_ids = var.vpc_security_group_ids
tags = var.common_tags
}