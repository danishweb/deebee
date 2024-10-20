class SchemaManager:
    def __init__(self):
        self.schemas = {}

    def define_schema(self, collection_name: str, schema: dict):
        """Define a schema for a specific collection."""
        self.schemas[collection_name] = schema

    def validate(self, collection_name: str, document: dict):
        """Validate a document against the schema."""
        schema = self.schemas.get(collection_name)
        if not schema:
            raise ValueError(f"No schema defined for collection '{collection_name}'.")

        for field, field_type in schema.items():
            print(field, field_type)
            if field not in document:
                raise ValueError(f"Field '{field}' is missing.")
            if not isinstance(document[field], field_type):
                raise ValueError(f"Field '{field}' must be of type '{field_type.__name__}'.")

