terraform {
required_providers {
aws = {
source = "hashicorp/aws"
version = "~> 5.0"
}
}


# Backend configuration should be provided in real usage for state isolation.
# backend "s3" {
# bucket = "my-terraform-state-bucket"
# key = "envs/prod/terraform.tfstate"
# region = "us-east-1"
# }
}


provider "aws" {
region = var.aws_region
# credentials should be sourced from environment or shared credentials file
}