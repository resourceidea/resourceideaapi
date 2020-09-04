from rest_framework.exceptions import APIException


class InvalidOperationException(APIException):
    """
    Exception raised an unacceptable operation is being performed.

    status_code: 400
    default_detail: Cannot perform an unacceptable operation
    default_code: invalid_operation
    """
    status_code = 400
    default_code = 'invalid_operation'
    default_detail = 'Can not perform an unacceptable operation'
