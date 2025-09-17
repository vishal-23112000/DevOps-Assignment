variable "name" { type = string }
variable "ami" { type = string }
variable "instance_type" { type = string default = "t3.micro" }
variable "subnet_id" { type = string }
variable "vpc_security_group_ids" { type = list(string) }
variable "tags" { type = map(string) default = {} }