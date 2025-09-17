resource "aws_db_subnet_group" "this" {
name = "${var.name}-subnet-group"
subnet_ids = var.subnet_ids
tags = var.tags
}


resource "aws_db_parameter_group" "this" {
name = "${var.name}-param-group"
family = var.family
description = "Custom parameter group for ${var.name}"


parameter {
name = "max_connections"
value = var.max_connections
}
}


resource "aws_db_instance" "this" {
identifier = var.identifier
engine = var.engine
engine_version = var.engine_version
instance_class = var.instance_class
allocated_storage = var.allocated_storage


name = var.db_name
username = var.username
password = var.password


parameter_group_name = aws_db_parameter_group.this.name
db_subnet_group_name = aws_db_subnet_group.this.name


skip_final_snapshot = true
vpc_security_group_ids = var.vpc_security_group_ids
tags = var.tags
}