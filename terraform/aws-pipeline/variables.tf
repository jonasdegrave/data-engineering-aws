variable "application" {
  type        = string
  description = "application name"
  default     = "stream-api"
}

variable "environment" {
  type        = string
  description = "environment name"
  default     = "development"
}

variable "aws_s3_bucket_destination" {
  type        = string
  description = "bucket arn"
  default     = "arn:aws:s3:::daredata-terraform-s3-bucket"
  //default     = "arn:aws:s3:::daredata-datalake"
}