# Mentor Candidate Test Task
[![Main workflow](https://github.com/EvgVol/test_mentor/actions/workflows/main.yml/badge.svg)](https://github.com/EvgVol/test_mentor/actions/workflows/main.yml)
[![Python Version](https://img.shields.io/badge/python-v3.11-blue)](https://www.python.org/downloads/release/python-3110/) [![Docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/) [![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/) [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13.0-336791?logo=postgresql&logoColor=white)](https://www.postgresql.org/)


This is a test task for candidates for the position of programming mentor. Presented here is a Telegram bot capable of performing various actions based on buttons and text commands, such as sending a photo or providing information upon request.

## Project Structure

```
.
├── bot.py                 # Main bot file
├── database.py            # Database handling
├── backup.sql             # Database backup file
├── settings.py            # Project settings
├── requirements.txt       # Project dependencies
├── Dockerfile             # Dockerfile for building application image
├── docker-compose.yml     # Docker Compose configuration for deployment
└── .github
    └── workflows
        └── main.yml       # GitHub Actions for CI/CD
```

## Prerequisites

To run and deploy the project locally, you’ll need to have the following installed:

* Python 3.10 or later
* PostgreSQL
* Telegram bot
* Yandex Cloud
* CI&CD
* Docker
* Docker Compose

## Installation and Running

1. Clone the repository:

```bash
git clone https://github.com/EvgVol/test_mentor.git
cd test_mentor
```

2. Install [PostgreSQL](https://postgrespro.ru/docs/postgresql/14/)

3. Create new database
```bash
CREATE DATABASE mentor;
-- Create user mentor_user and come up with your own password instead of xyzzyyzzz
CREATE USER mentor_user WITH ENCRYPTED PASSWORD 'xxxyyyzzz'; 
-- Grant mentor_user all privileges on mentor database 
GRANT ALL PRIVILEGES ON DATABASE mentor TO mentor_user;   
```
4. Load data from `backup.sql` into new database. [Documentation](https://www.postgresql.org/docs/14/app-pgrestore.html)

5. Create a `.env` file with the necessary environment variables:

```bash
touch .env
```
Add the following environment variables to the `.env` file:

```
TELEGRAM_TOKEN='YOUR_TELEGRAM_BOT_TOKEN'
DB_NAME='YOUR_DB_NAME'
POSTGRES_USER='YOUR_POSTGRES_USERNAME'
POSTGRES_PASSWORD='YOUR_POSTGRES_PASSWORD'
DB_HOST='YOUR_DB_DOMAIN_OR_IP_ADDRESS'
DB_PORT='YOUR_DB_PORT'
```

6. Run the project using Docker Compose:

```bash
docker-compose up -d
```

Now your Telegram bot is ready to use and available for interaction.

**Note:** Don't forget to replace `YOUR_TELEGRAM_BOT_TOKEN` and other environment variables with actual values.

## CI/CD with GitHub Actions

This project uses GitHub Actions for building and deploying the Docker image of the application to your server. To configure this, you can set up repository secrets in the "Settings -> Secrets" section. The necessary environment variables are:

- DOCKER_USERNAME: your Docker Hub username
- DOCKER_PASSWORD: your Docker Hub password
- HOST_DEV: hostname or IP address of the deployment server
- USER_DEV: username on the server
- SSH_KEY: your private SSH key for access to the server
- PASSPHRASE: password for your private SSH key (if any)
- TELEGRAM_TOKEN, DB_NAME, POSTGRES_USER, POSTGRES_PASSWORD, DB_HOST, DB_PORT: application environment variables as described earlier

GitHub Actions will automatically carry out all necessary operations for building, publishing, and deploying your project upon each `git push` to the `main` branch.

## Contributing

If you have any questions, suggestions, requests, or comments, please feel free to open [issues or pull requests](https://github.com/EvgVol/test_mentor/issues) in this repository.