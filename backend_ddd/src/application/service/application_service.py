from application.src.interaction.query.query import Query
from application.src.interaction.query.query_response import QueryResponse


class ApplicationService(object):

    def execute(
            self,
            query: Query
    ) -> QueryResponse:
        pass
