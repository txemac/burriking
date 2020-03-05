from typing import Dict

from user_interface.api_action import ApiAction


class HealthAction(ApiAction):

    def execution(
            self
    ) -> Dict:
        return dict(status='OK')
