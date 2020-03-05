from typing import Dict
from typing import List
from typing import Union

from flask import Request
from werkzeug.local import LocalProxy

from user_interface.http.server_request import ServerRequest


def get_query_params(
        request: Union[Request, object]
) -> Dict[str, Union[str, int, List[Union[str, int]]]]:
    """
    Get the arguments from a GET request, supporting the type list like "genders[]=male&genders[]=female"

    :param request: GET request
    :return: Dict
    """
    if type(request) is LocalProxy:
        args = request.args.to_dict(flat=False)
    elif type(request) is ServerRequest:
        args = request.query_params()

    result = dict()
    for key in args.keys():
        if '[]' in key:
            result[key[:-2]] = args[key]
        else:
            result[key] = args[key][0]
    return result
