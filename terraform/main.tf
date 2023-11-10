provider "aws" {
  region = "us-east-1" # or your preferred region
}

resource "aws_instance" "fastapi_ec2" {
  ami           = "ami-0fc5d935ebf8bc3bc" # replace with the latest Ubuntu AMI in your region
  instance_type = "t2.micro"

  tags = {
    Name = "FastAPI-EC2"
  }

  key_name = aws_key_pair.deployer.key_name

  security_groups = [aws_security_group.fastapi_sg.name]
  user_data       = file("setup.sh") # path to the script

}

resource "aws_security_group" "fastapi_sg" {
  name = "fastapi_sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # replace with your IP for SSH access to be more secure
  }

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # allows API traffic from any IP
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
