class QueryResponse:

    def __init__(self, data: list = [], metadata: dict = {}):
        self._data = data
        self._metadata = metadata

    def metadata(self) -> dict:
        return self._metadata

    def data(self) -> list:
        return self._data
