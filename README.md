# MyProject Deployment

This repository contains the solution for deploying a Django application with a PostgreSQL database, using Nginx as a reverse proxy. The deployment is automated with Ansible, and it includes a basic healthcheck API for monitoring the system's status.

## Project Structure

```plaintext
myproject-deployment/
│
├── ansible/
│   ├── playbook.yml               # Main Ansible playbook
│   ├── inventory/
│   │   └── hosts.ini             # Inventory file with server configuration
│   ├── roles/
│   │   ├── django/
│   │   │   └── tasks/main.yml    # Django installation and configuration
│   │   ├── nginx/
│   │   │   └── tasks/main.yml    # Nginx setup and configuration
│   │   └── postgresql/
│   │       └── tasks/main.yml    # PostgreSQL installation and setup
│   └── templates/
│       └── nginx.conf.j2         # Jinja2 template for Nginx config
│
├── django/
│   └── healthcheck_urls.py       # Django healthcheck API
│
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```
### Ansible Playbook

The ansible/playbook.yml file is responsible for setting up the entire application stack on an Ubuntu server. It installs the following components:

    Django with Django REST Framework.

    PostgreSQL as the database.

    Nginx as a reverse proxy in front of Django.

The playbook is idempotent, meaning it can be run multiple times without causing errors or inconsistent states.
Running the Playbook

## To run the Ansible playbook:

    Ensure you have Ansible installed on your local machine. If not, you can install it via pip:
```
pip install ansible
```
## Clone the repository:
```
git clone https://github.com/Bun4un/devops_test_tasks.git
cd devops_test_tasks/ansible
```
Configure your Ansible inventory file (e.g., hosts) with your target server's IP address or hostname.

## Run the playbook:

    ansible-playbook -i hosts ansible/playbook.yml

## Django Healthcheck API

The django/healthcheck_urls.py file defines a simple healthcheck API endpoint that checks the operational status of the key components:
    - Nginx: Ensures the Nginx service is active.
    - Django: Verifies the Django application can connect to the PostgreSQL database.
    - PostgreSQL: Checks if PostgreSQL is running and accessible by Django.

## Healthcheck Endpoint

The healthcheck endpoint can be accessed at:

#### GET /healthcheck/

It returns a JSON response indicating the status of each component:
```
{
  "status": "OK",
  "components": {
    "nginx": "running",
    "django": "running",
    "postgresql": "running"
  }
}
```
Example Healthcheck Response

If all components are running, the response will look like:
```
{
  "status": "OK",
  "components": {
    "nginx": "running",
    "django": "running",
    "postgresql": "running"
  }
}
```
If any component is down, the status will be marked as "not running".
Requirements

To run the Django application and deploy the stack, you need to install the following dependencies:

Install the Python dependencies:

    pip install -r requirements.txt

## Dependencies

requirements.txt contains the following packages:

Django>=4.0,<5.0
psycopg2>=2.9,<3.0
gunicorn>=20.0,<21.0

    Django: The web framework for building the application.

    psycopg2: PostgreSQL database adapter for Python.

    gunicorn: WSGI HTTP server for running Django in production.

Nginx Configuration

The ansible/nginx_config file contains the configuration for setting up Nginx as a reverse proxy for the Django application. It forwards requests to the Django application running with Gunicorn.
Additional Notes

The playbook and configuration are designed to work on Ubuntu 24.04.
Ensure that your PostgreSQL database is properly configured and accessible by Django.
For production, it's recommended to set up proper SSL certificates for Nginx using Let's Encrypt or any other certificate authority.
