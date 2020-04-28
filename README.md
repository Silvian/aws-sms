# aws-sms
SMS Service using AWS Lambda function and SNS.

### Installation:

Checkout the project:
- `git clone`

Create a virtual environment and install requirements:

- `python3 -m venv venv`
- `pip install -r requirements.txt`
- `mkdir lib`
- `pip install -t lib/ phonenumbers`

Build an aws lambda deployable artifact:

- `zip -r ../aws.zip . *`
