variable "bucket_name" { type = string }
variable "acl" { type = string default = "private" }
variable "versioning" { type = bool default = true }
variable "tags" { type = map(string) default = {} }