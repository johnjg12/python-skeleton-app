# EC2

You can use free tier t2.micro ec2 instances to host your API endpoint for PoC or early development.  
See the [terraform README.md](..%2F..%2F..%2Fterraform%2FREADME.md) if you just want to get one up and running as
quickly as possible.

Otherwise you can ask ChatGPT or [Python API Generator](https://chat.openai.com/g/g-PRk40O4g9-python-api-generator)

```
show me how to set up an ec2 instance in AWS with my python fastapi app that is in a git repo and run on docker.
```   

and that should get you close. but you can adjust the prompt and add any of your additional requirements to get a custom
walkthrough.

Example of above prompt from 2023-11-10

Alright, let's jack into the Matrix and get your FastAPI app running on an EC2 instance in AWS with Docker. This is
going to be a multi-step process, so grab your sunglasses, and let's dive in.

**Step 1: Setting Up Your EC2 Instance in AWS**

1. **Login to AWS Console**: Access the AWS Management Console and log in.
2. **Launch an EC2 Instance**:
    - Go to the EC2 dashboard and click "Launch Instance".
    - Choose an Amazon Machine Image (AMI) - for Docker, a general-purpose Linux AMI like Amazon Linux 2 is a good
      choice.
    - Select an Instance Type - depending on your app's needs, a `t2.micro` might suffice for starters (and it's
      free-tier eligible).
    - Configure Instance Details as needed. For most basic apps, the defaults are fine.
    - Add Storage if needed. The default size should be enough to get started.
    - Configure the Security Group to set up network access. Make sure to allow HTTP (port 80) and HTTPS (port 443), and
      SSH (port 22) for your IP.
    - Review and launch the instance. You'll be prompted to create or select an existing key pair. Download this key
      pair and keep it safe – you'll need it for SSH access.

**Step 2: Installing Docker on Your EC2 Instance**

1. **SSH into Your EC2 Instance**:
    - Use the downloaded key pair and the public DNS/IP of your EC2 instance.
    - The command will look something like `ssh -i /path/to/your-key.pem ec2-user@your-instance-public-dns`.
2. **Install Docker**:
    - Update the package database: `sudo yum update -y`
    - Install Docker: `sudo yum install docker -y`
    - Start the Docker service: `sudo service docker start`
    - Add the `ec2-user` to the Docker group to execute Docker commands without
      using `sudo`: `sudo usermod -a -G docker ec2-user`
    - Log out and log back in again to pick up the new Docker group permissions.

**Step 3: Pulling Your FastAPI App from Git and Running it on Docker**

1. **Install Git** (if not already installed): `sudo yum install git -y`
2. **Clone Your Git Repository**:
    - `git clone https://your-repository-url.git`
    - Navigate to the cloned directory: `cd your-repository-name`
3. **Running Your App with Docker**:
    - Make sure you have a `Dockerfile` in your repository.
    - Build the Docker image: `docker build -t your-app-name .`
    - Run the Docker container: `docker run -d --name your-app-container -p 80:80 your-app-name`

Your FastAPI app should now be running on your EC2 instance, accessible via the public IP or DNS of the instance.

Remember, this is like a basic training program – there's a lot more to learn about AWS, EC2, and Docker. Always ensure
your setup is secure, especially when exposing ports and managing security groups. If anything seems off, feel free to
ask for more guidance.
