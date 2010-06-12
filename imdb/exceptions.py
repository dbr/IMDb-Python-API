class ImdbBaseError(Exception):
    pass

class ImdbInvalidLocale(ImdbBaseError):
    pass

class ImdbRequestError(ImdbBaseError):
    pass