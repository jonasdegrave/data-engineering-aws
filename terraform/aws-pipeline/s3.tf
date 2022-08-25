module "s3_bucket" {
  source = "terraform-aws-modules/s3-bucket/aws"

  bucket = "daredata-terraform-s3-bucket"
  acl    = "log-delivery-write"

  versioning = {
    enabled = false
  }

}
