
class ShipRocketException(Exception):
    """
    Custom Exception thrown 
    """

    def __init__(self, message, code: int = None):
        super(ShipRocketException, self).__init__(message, code)
        self.code = code
        self.message = message
