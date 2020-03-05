from abc import abstractmethod

from application.src.interaction.transformer.transformer import Transformer
from user_interface.server_request_interface import ServerRequestInterface


class CommandTransformer(Transformer):

    def transforms_to(
            self,
    ):
        return self.__class__.__name__

    @abstractmethod
    def transform_request(
            self,
            request: ServerRequestInterface,
    ):
        pass
