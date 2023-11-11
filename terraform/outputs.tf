output "ec2_public_ip" {
  value = aws_instance.fastapi_ec2.public_ip
}

output "fast_api_api_url" {
  value = "http://${aws_instance.fastapi_ec2.public_ip}:${var.fastapi_public_port}"
}