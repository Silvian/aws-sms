import phonenumbers

from exceptions import InvalidNumberException, ParsingException


def parse_phone_number(phone, country_code=None):
    try:
        number = phonenumbers.parse(number=phone, region=country_code)
    except phonenumbers.phonenumberutil.NumberParseException as e:
        raise ParsingException(phone, e)

    if not phonenumbers.is_valid_number(number):
        raise InvalidNumberException(phone)

    formatted_number = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)
    return formatted_number
