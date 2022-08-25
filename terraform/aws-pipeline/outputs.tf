output "api_server_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.api_server.public_ip
}

/*
output "kinesis_firehose_delivery_stream_arn" {
  description = "The ARN of the Kinesis Data Firehose Delivery Stream"
  value       = aws_kinesis_firehose_delivery_stream.main.arn
}

output "kinesis_firehose_delivery_stream_name" {
  description = "The name of the Kinesis Data Firehose Delivery Stream"
  value       = aws_kinesis_firehose_delivery_stream.main.name
}
*/