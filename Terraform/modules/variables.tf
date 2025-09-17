variable "aws_region" { type = string default = "us-east-1" }


# General tags
variable "common_tags" {
type = map(string)
default = {
ManagedBy = "terraform"
Project = "devops-assignment"
}
}


# Example placeholders for subnet/security group ids for mock setup
variable "public_subnet_id" { type = string default = "subnet-0123456789abcdef0" }
variable "private_subnet_ids" { type = list(string) default = ["subnet-0aaa111bbb222ccc"] }
variable "vpc_security_group_ids" { type = list(string) default = ["sg-0123456789abcdef0"] }