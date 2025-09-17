resource "aws_iam_role" "ec2_role" {
name = "${var.name}-ec2-role"
assume_role_policy = data.aws_iam_policy_document.ec2_assume_role.json
}


data "aws_iam_policy_document" "ec2_assume_role" {
statement {
actions = ["sts:AssumeRole"]
principals {
type = "Service"
identifiers = ["ec2.amazonaws.com"]
}
}
}


resource "aws_iam_role_policy_attachment" "s3_access" {
role = aws_iam_role.ec2_role.name
policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
}


resource "aws_instance" "this" {
ami = var.ami
instance_type = var.instance_type
subnet_id = var.subnet_id
vpc_security_group_ids = var.vpc_security_group_ids
iam_instance_profile = aws_iam_instance_profile.ec2_profile.name
tags = var.tags
}


resource "aws_iam_instance_profile" "ec2_profile" {
name = "${var.name}-instance-profile"
role = aws_iam_role.ec2_role.name
}