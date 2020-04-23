

class InvalidNumberException(Exception):
    """Invalid number exception."""

    def __init__(self, phone):
        self.phone = phone

    def __str__(self):
        return "Invalid phone number: {}".format(self.phone)


class ParsingException(Exception):
    """Parsing exception."""

    def __init__(self, phone, message):
        self.phone = phone
        self.message = message

    def __str__(self):
        return 'Parsing Exception: "{}" for number: {}'.format(
            self.message, self.phone
        )
