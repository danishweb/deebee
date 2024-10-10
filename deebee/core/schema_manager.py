class SchemaManager:
    def __init__(self):
        self.schemas = {}

    def define_schema(self, collection_name, schema):
        """Define a schema for a specific collection."""
        self.schemas[collection_name] = schema

    def validate(self, collection_name, document):
        """Validate a document against its schema."""
        schema = self.schemas.get(collection_name)
        if schema:
            for field, field_type in schema.items():
                if field not in document or not isinstance(document[field], field_type):
                    raise ValueError(f"Field '{field}' is missing or not of type '{field_type.__name__}'.")