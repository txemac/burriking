from abc import ABC
from abc import abstractmethod


class Query(ABC):
    _MESSAGE_TYPE = 'query'

    @abstractmethod
    def error_message(self):
        pass

    def message_type(self):
        return self._MESSAGE_TYPE
