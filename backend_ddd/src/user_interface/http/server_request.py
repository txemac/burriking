from user_interface.server_request_interface import ServerRequestInterface


class ServerRequest(ServerRequestInterface):

    def __init__(self, server_request: object):
        self.__server_request = server_request
        self.__query_params = dict()
        self.__view_args = dict()

        if len(self.__server_request.args):
            from infrastructure.user_interface.utils import get_query_params
            self.__query_params = get_query_params(request=server_request)

        if self.__server_request.view_args is not None:
            self.__view_args = self.__server_request.view_args

    def query_params(self) -> dict:
        return self.__query_params

    def view_args(self) -> dict:
        return self.__view_args

    def parsed_body(self) -> dict:
        return self.__server_request.get_json()
