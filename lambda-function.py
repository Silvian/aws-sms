import boto3


def send_to_sns(request, context):
    """
    Lambda function to trigger sns service to send sms.
    
    Example request:
    {
        "phone": "+0123456789"
        "message": "Sample message text."
    }
    """

    sns = boto3.client('sns')
    
    print("Sending sms message: {} to: {}".format(
        request['message'], request['phone'])
    )
    
    sns.publish(
        PhoneNumber=request['phone'],
        Message=request['message'],
    )
    
    return {"success": True}
