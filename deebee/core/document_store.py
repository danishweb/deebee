import uuid
from .persistence_layer import PersistenceLayer
from .schema_manager import SchemaManager
from deebee.config.settings import base_collection_folder

class DocumentStore:
    def __init__(self, collection_name: str, base_path: str = base_collection_folder):
        self.collection_name = collection_name
        self.collection_path = f"{base_path}/{collection_name}.json"
        self.schema_manager = SchemaManager()  
        self.documents = self.load_documents()

    def load_documents(self):
        """Load documents from the collection."""
        return PersistenceLayer.read_json(self.collection_path)

    def save_documents(self):
        """Save documents to the collection."""
        PersistenceLayer.write_json(self.collection_path, self.documents)

    def insert(self, document: dict):
        """Insert a new document after schema validation."""
        if self.schema_manager.schemas.get(self.collection_name) is not None:
            self.schema_manager.validate(self.collection_name, document)  # Validation
        document['_id'] = str(uuid.uuid4())
        self.documents.append(document)
        self.save_documents()

    def find(self, query: dict):
        """Find documents matching the query."""
        return [doc for doc in self.documents if all(doc.get(k) == v for k, v in query.items())]

    def delete(self, document_id: str):
        """Delete a document by ID."""
        self.documents = [doc for doc in self.documents if doc['_id'] != document_id]
        self.save_documents()
