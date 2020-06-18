import boto3

from exceptions import InvalidNumberException, ParsingException
from parsers import parse_phone_number


def handler(request, context):
    """
    Lambda function to trigger sns service to send sms.
    
    Example request:
    {
        "phone": "+44123456789",
        "country_code": "GB",
        "sender_id": "Sender Name",
        "message": "Sample message text."
    }
    """

    sns = boto3.client('sns')
    phone = request.get('phone')
    country_code = request.get('country_code')
    sender_id = request.get('sender_id')
    message = request.get('message')

    if not phone:
        return {"message": "Missing phone number."}

    if not message:
        return {"message": "Missing message body."}

    try:
        phone_number = parse_phone_number(phone, country_code)
    except (InvalidNumberException, ParsingException) as e:
        return {"message": str(e)}

    print('Sending sms message: "{}" to: {}'.format(message, phone_number))

    message_attributes = {}
    if sender_id:
        message_attributes = {
            'AWS.SNS.SMS.SenderID': {
                'DataType': 'String',
                'StringValue': sender_id,
            }
        }

    sns.publish(
        PhoneNumber=phone_number,
        Message=message,
        MessageAttributes=message_attributes,
    )

    return {"success": True}
