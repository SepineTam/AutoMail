# AutoMail

This project is a Python script for automating the sending of emails using Gmail. The script can be deployed on an AWS EC2 instance and scheduled to run at specific intervals using `crontab`.

# How to use

## Install Project

### Clone the Repository
First, clone the project repository to your local machine:

```bash
cd documents/github  # you could change it for yourself
git clone https://github.com/zXiaoyuLuo/AutoMail.git
```

### Create a Virtual Environment
Navigate to the project directory, then create and activate a virtual environment:

```bash
cd your_repository_position
python -m venv venv
source venv/bin/activate
# For Windows, use next line
# venv\Scripts\activate
```

### Install Dependencies
Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

### Configure Environment Variables

Create a .env file in the project root directory and add the following content:

Or you could change '.env.demo' file to '.env' and change the file body

it looks like ⬇️
```
# .env
USERNAME=YOUR_NAME
SMTP_SERVER=smtp.shu.edu.cn
SMTP_PORT=465
EMAIL_USERNAME=your_address@shu.edu.cn
EMAIL_PASSWORD=your_password
RECIPIENT_EMAIL=recipient@example.com
RECIPIENT_EMAIL=xiaoyuluowork@gmail.com
LOG_PATH=.log
```


## Run the Project
Run the main program file:

```bash
python main.py
```



