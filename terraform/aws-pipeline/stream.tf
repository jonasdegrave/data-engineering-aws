
module "kinesis_stream" {
  source = "dod-iac/kinesis-stream/aws"

  name = format("app-%s-%s", var.application, var.environment)
  tags = {
    Application = var.application
    Environment = var.environment
    Automation  = "Terraform"
    }

}


module "kinesis_firehose_s3_bucket" {
  source  = "dod-iac/kinesis-firehose-s3-bucket/aws"

  //name = format("app-%s-firehose-%s", var.application, var.environment)
  name = "daredata-terraform-kinesis-firehose"

  kinesis_stream_arn = module.kinesis_stream.arn
  kinesis_role_name = format("app-%s-firehose-source-%s", var.application, var.environment)

  s3_bucket_arn = var.aws_s3_bucket_destination
  s3_role_name = format("app-%s-firehose-destination-%s", var.application, var.environment)

  /*
  parameters = { 
    DeliveryStreamType  = "DirectPut"
  }
  */

  tags = {
    Application = var.application
    Environment = var.environment
    Automation  = "Terraform"
  }
}