from flask import request as flask_request

from application.service.application_service import ApplicationService
from user_interface.action.action_interface import ActionInterface
from user_interface.http.server_request import ServerRequest


class ApiAction(ActionInterface):

    def __init__(
            self,
            service: ApplicationService = None
    ):
        self._service = service

    def handle(self):
        return self.execution()

    def execution(self):
        pass

    def _get_server_request(self):
        return ServerRequest(flask_request)
