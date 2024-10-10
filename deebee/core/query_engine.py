class QueryEngine:
    @staticmethod
    def query(documents, conditions):
        """Query documents based on conditions."""
        return [doc for doc in documents if all(doc.get(k) == v for k, v in conditions.items())]