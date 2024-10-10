import json
import os
import uuid

class DocumentStore:
    def __init__(self, collection_name: str, base_path="collections"):
        self.collection_name = collection_name
        self.collection_path = os.path.join(base_path, f"{collection_name}.json")
        self.load_documents()

    def load_documents(self):
        """Load documents from the collection."""
        if os.path.exists(self.collection_path):
            with open(self.collection_path, 'r') as f:
                # Load the documents and ensure it's a list
                data = json.load(f)
                self.documents = data if isinstance(data, list) else []
        else:
            self.documents = []

    def save_documents(self):
        """Save documents to the collection."""
        with open(self.collection_path, 'w') as f:
            json.dump(self.documents, f, indent=4)

    def insert(self, document):
        """Insert a new document."""
        document['_id'] = str(uuid.uuid4())
        self.documents.append(document)
        self.save_documents()

    def find(self, query):
        """Find documents matching the query."""
        return [doc for doc in self.documents if all(doc.get(k) == v for k, v in query.items())]

    def delete(self, document_id):
        """Delete a document by ID."""
        self.documents = [doc for doc in self.documents if doc['_id'] != document_id]
        self.save_documents()

