# AutoMail

这个项目是一个用于使用 Gmail 自动发送电子邮件的 Python 脚本。该脚本可以部署在 AWS EC2 实例上，并使用 `crontab` 定时运行。

## 语言
- [English](README.md)
- [简体中文](README_zh.md)

# 使用说明

## 安装项目

### 克隆代码仓库
首先，将项目仓库克隆到本地计算机：

```bash
cd documents/github  # 你可以根据需要更改此路径
git clone https://github.com/zXiaoyuLuo/AutoMail.git
```

### 创建虚拟环境
导航到项目目录，然后创建并激活虚拟环境：

```bash
cd your_repository_position
python -m venv venv
source venv/bin/activate
# 对于 Windows，使用以下命令
# venv\Scripts\activate
```

### 安装依赖
使用 pip 安装所需的依赖项：

```bash
pip install -r requirements.txt
```

## 使用

### 配置环境变量

在项目根目录创建一个 `.env` 文件，并添加以下内容：

或者你可以将 `.env.demo` 文件改名为 `.env`，并更改文件内容

文件内容如下⬇️
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

## 运行项目
运行主程序文件：

```bash
python main.py
```
