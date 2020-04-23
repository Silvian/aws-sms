import boto3

from exceptions import InvalidNumberException, ParsingException
from parsers import parse_phone_number


def handler(request, context):
    """
    Lambda function to trigger sns service to send sms.
    
    Example request:
    {
        "phone": "+44123456789",
        "countryCode": "GB",
        "message": "Sample message text."
    }
    """

    try:
        sns = boto3.client('sns')
        message = request.get('message')
        phone_number = parse_phone_number(request.get('phone'), request.get('country_code'))
    except (InvalidNumberException, ParsingException) as e:
        return {"message": str(e)}
    
    print('Sending sms message: "{}" to: {}'.format(message, phone_number))
    
    sns.publish(PhoneNumber=phone_number, Message=message)
    
    return {"success": True}
