resource "aws_s3_bucket" "this" {
bucket = var.bucket_name
acl = var.acl


versioning {
enabled = var.versioning
}


lifecycle_rule {
id = "transition-to-glacier"
enabled = true


transition {
days = 30
storage_class = "GLACIER"
}


noncurrent_version_transition {
days = 30
storage_class = "GLACIER"
}
}


tags = var.tags
}


# Optional server-side encryption
resource "aws_s3_bucket_server_side_encryption_configuration" "this" {
bucket = aws_s3_bucket.this.id


rule {
apply_server_side_encryption_by_default {
sse_algorithm = "AES256"
}
}
}