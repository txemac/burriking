from typing import Dict

from infrastructure.user_interface import responder
from user_interface.api_action import ApiAction


class HealthAction(ApiAction):

    def execution(
            self
    ) -> Dict:
        return responder.generate_get(
            message='OK',
        )
