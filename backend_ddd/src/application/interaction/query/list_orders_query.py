from datetime import date

from application.src.interaction.query.query import Query


class ListOrdersQuery(Query):

    def __init__(
            self,
            barista: str,
            start_date: date,
            end_date: date,
    ):
        self.__barista = barista
        self.__start_date = start_date
        self.__end_date = end_date

    def error_message(
            self
    ):
        pass

    def message_type(
            self
    ):
        pass

    def barista(self):
        return self.__barista

    def start_date(self):
        return self.__start_date

    def end_date(self):
        return self.__end_date
