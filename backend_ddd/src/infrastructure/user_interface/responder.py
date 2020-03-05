from functools import partial
from http import HTTPStatus
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from flask import jsonify
from flask import make_response
from requests import Response

"""
Module maker responses with the json standard of the APIs.

Example:
{
    "status": {
        "text": "Order created"
    },
    "data": [{
        "barista": "Txema",
    }]
}

"""


def _generate_response(
        data: Optional[object] = None,
        message: str = 'ok',
        status_code: int = HTTPStatus.OK,
) -> Response:
    """
    Generate full responses.

    :param List data: list with the data
    :param String message: text
    :param Integer status_code: status code of the response
    :return Response: response
    """
    # full body at response
    body = _generate_body(data, message)

    # create response
    response = make_response(jsonify(body))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT, DELETE, PATCH'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.status_code = status_code
    return response


def _generate_body(
        data: Optional[Any] = None,
        message: str = 'ok',
) -> Dict[str, Union[Dict[str, str], Dict[str, int], List[Any]]]:
    """
    Generate a body response as API documentation.

    :param List data: data
    :param String message: message
    :return Dict: body
    """
    return dict(
        status=dict(
            text='ok' if message is None else message
        ),
        data=[data] if type(data) != list else data
    )


generate_get = partial(_generate_response, status_code=HTTPStatus.OK)
generate_post = partial(_generate_response, status_code=HTTPStatus.CREATED)
