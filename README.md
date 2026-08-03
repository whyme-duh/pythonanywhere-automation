# PythonAnywhere Automation

## Project Overview

This project automates interactions with PythonAnywhere, a cloud-based Python hosting platform. The automation script handles account management, deployment, and configuration tasks programmatically, enabling streamlined workflow management without manual web interface interactions.

## Features

- Automated PythonAnywhere account operations
- Programmatic web scraping and automation
- Secure credential management through environment variables
- Support for multiple user accounts

## Environment Configuration (.env File)

This project uses a `.env` file to securely store sensitive credentials. The `.env` file should be created in the project root directory and contains account credentials for PythonAnywhere.

### .env File Format

Create a `.env` file with the following structure containing a dictionary of usernames and passwords:

```
ACCOUNTS={
    "username1": "password1",
    "username2": "password2",
    "username3": "password3"
}
```

### Example .env File

```
ACCOUNTS={
    "john_doe": "secure_password_123",
    "jane_smith": "another_secure_pwd",
    "admin_user": "admin_password_456"
}
```

## Setup Instructions

1. Clone or download the project repository
2. Create a `.env` file in the project root directory
3. Add your PythonAnywhere account credentials in the format shown above
4. Install required dependencies using `requirements.txt`: `pip install -r requirements.txt`
   - This will install all necessary modules including `python-dotenv`, `selenium`, and other dependencies
5. Run the automation script `python automateReload.py`

## Important Security Notes

- **Never commit the `.env` file to version control**
- Add `.env` to your `.gitignore` file
- Keep your credentials secure and never share them
- Ensure `.env` file permissions are restricted (readable only by owner)

## Requirements

- Python 3.6+
- python-dotenv
- Selenium or similar web automation library

## License

This project is provided as-is for automation purposes.
