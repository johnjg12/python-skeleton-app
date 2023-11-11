provider "aws" {
  region = var.default_region # or your preferred region
}

resource "aws_instance" "fastapi_ec2" {
  ami           = var.ami
  instance_type = var.instance_type

  tags = {
    Name = var.app_name
  }

  key_name = aws_key_pair.deployer.key_name

  security_groups = [aws_security_group.fastapi_sg.name]
  user_data       = file("setup.sh") # path to the script

}

resource "aws_security_group" "fastapi_sg" {
  name = "fastapi_sg"

  # allow SSH access (recommended to use EC2 instance connect)
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.subnet_allow_to_ssh] # replace with your IP for SSH access to be more secure
  }

  ingress {
    from_port   = var.fastapi_public_port
    to_port     = var.fastapi_private_port
    protocol    = "tcp"
    cidr_blocks = [var.subnet_allow_to_api] # allows API traffic from any IP
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_key_pair" "deployer" {
  key_name   = "ec2-key-pair"
  public_key = file("ec2-public-ssh-key.pub") # put your public key in this file
}
