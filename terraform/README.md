# FastAPI Deployment on AWS using Terraform

This project automates the deployment of a FastAPI application onto an AWS EC2 instance using Terraform. It sets up the
required infrastructure, including the EC2 instance, security groups, and deploys the FastAPI application using Docker.

## Prerequisites

Before you begin, ensure you have the following:

- AWS account and AWS CLI configured with access keys.
- Terraform installed on your machine.
- SSH key pair for AWS EC2 access (public and private keys).

## Quick Start

To quickly start the deployment, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/johnjg12/python-skeleton-app.git
   cd python-skeleton-app/terraform
   cp variables.tf.example variables.tf
   ```

Note: Modify `variables.tf` to your liking.  
Next, you need a public ssh key to add to the ec2 instance so you can ssh to it.
Copy that to this directory and name it `ec2-public-ssh-key.pub`.

Hint: if you need to generate a public key from a private key (i.e. a `.pem` file downloaded from aws console), run the
following:

```bash
KEY_PATH=/path/to/my-private-key.pem
ssh-keygen -y -f "$KEY_PATH" > ec2-public-ssh-key.pub
```

2. **Set Up Your AWS Credentials**

   Make sure your AWS credentials are configured. This can be done via the AWS CLI:

   ```bash
   aws configure
   ```

3. **Initialize Terraform**

   Initialize a working directory containing Terraform configuration files.

   ```bash
   terraform init
   ```

4. **Apply Terraform Configuration**

   Apply the Terraform configuration to start the deployment. When prompted, confirm with `yes`.

   ```bash
   terraform apply
   ```

5. **Access Your FastAPI Application**

   After the deployment, Terraform will output the public IP of the EC2 instance. Use this IP in your browser to access
   the FastAPI application.

   ```bash
   http://<EC2-instance-public-IP>:<fastapi_public_port>
   ```

## Configuration

- **Security Groups**: By default, the security group allows SSH (port 22) and HTTP (port 80) access. Modify the
  security group in `main.tf` for additional configurations.
- **FastAPI Application**: Ensure your FastAPI application is in a Git repository and update the `setup.sh` script with
  its URL.
- **EC2 Key Pair**: Replace the placeholder in `main.tf` with the path to your public key file.

## Additional Information

- **AWS Region**: The default AWS region is set in `main.tf`. Change it as per your requirement.
- **Instance Type**: The default is `t2.micro`, which is eligible for the AWS free tier.
