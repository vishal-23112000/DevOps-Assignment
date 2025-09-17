variable "name" { type = string }
variable "identifier" { type = string }
variable "engine" { type = string }
variable "engine_version" { type = string }
variable "family" { type = string }
variable "instance_class" { type = string }
variable "allocated_storage" { type = number }
variable "username" { type = string }
variable "password" { type = string }
variable "db_name" { type = string }
variable "subnet_ids" { type = list(string) }
variable "vpc_security_group_ids" { type = list(string) }
variable "max_connections" { type = string default = "100" }
variable "tags" { type = map(string) default = {} }