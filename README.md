# Flask AWS Deployment Guide

This guide will help you deploy your Flask application on an EC2 instance using Docker and Docker Compose.

## Prerequisites

- AWS account
- Basic knowledge of AWS EC2, Docker, and Docker Compose

## Steps to Deploy

### 1. Launch EC2 Instance

1. Open the AWS Management Console.
2. In the search bar, type `EC2` and select it.
3. Click on `Launch Instance`.

### 2. Configure Instance Details

4. **Name and Tags**: Enter a name for your instance.
5. **Application and OS Images (AMI)**: Select `Ubuntu` as the OS.
6. **Instance Type**: Choose `t2.micro`.

### 3. Configure Key Pair

7. Click on `Create new key pair`.
8. Enter a name for your key pair, keep everything as default, and click `Create`.

### 4. Configure Network Settings

9. In the network settings section, click `Edit`.
10. Click on `Create new security group`.
11. Check the boxes for `Allow HTTP traffic` and `Allow SSH traffic`.
12. Click on `Add security group rule`.
13. Set the following values:
    - **Type**: Custom TCP
    - **Port range**: 5555
    - **Source type**: Anywhere
14. Click `Launch instance`.

### 5. Connect to Your Instance

15. Go to your EC2 dashboard, select the instance you just created, and click `Connect`.
16. Follow the instructions to connect to your instance using SSH.

### 6. Clone the Repository

17. Once inside the EC2 instance, run the following command to clone the repository:
    ```bash
    git clone https://github.com/waleed399/flask-aws.git
    ```
18. Change directory to the project folder:
    ```bash
    cd flask-aws
    ```

### 7. Install Docker

19. Run the following commands to install Docker:
    ```bash
    sudo apt update
    sudo apt install apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt update
    sudo apt install docker-ce
    sudo systemctl start docker
    ```

### 8. Install Docker Compose

20. Run the following commands to install Docker Compose:
    ```bash
    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    docker-compose --version
    ```

### 9. Deploy the Flask Application

21. Run the Docker Compose command inside the EC2 instance:
    ```bash
    sudo docker-compose up
    ```

### 10. Access Your Flask Application

22. Your Flask app is now up and running. You can access it through the following URL:
    ```
    http://YOUR_INSTANCE_IP:5555
    ```

## Conclusion

You've successfully deployed your Flask application on an EC2 instance using Docker and Docker Compose. Happy coding!

---

Feel free to reach out if you have any questions or need further assistance.
