import json
import os
import uuid
from deebee.config.settings import base_path

class DocumentStore:
    def __init__(self, collection_name: str, base_path: str=base_path):
        self.collection_name = collection_name
        self.collection_path = os.path.join(base_path, f"{collection_name}.json")
        self.load_documents()

    def load_documents(self):
        """Load documents from the collection."""
        try:
            if os.path.exists(self.collection_path):
                with open(self.collection_path, 'r') as f:
                    data = json.load(f)           
                    self.documents = data if isinstance(data, list) else []
            else:
                self.documents = []
        except json.JSONDecodeError:
            # Handle case where the JSON file is corrupted or empty
            print(f"Warning: The file {self.collection_path} is not valid JSON.")
            self.documents = []
        except Exception as e:
            # Catch any other exceptions for debugging purposes
            print(f"Error loading documents: {e}")
            self.documents = []

    def save_documents(self):
        """Save documents to the collection."""
        with open(self.collection_path, 'w') as f:
            json.dump(self.documents, f, indent=4)

    def insert(self, document):
        """Insert a new document."""
        if not isinstance(document, dict):
            raise ValueError("Document must be a dictionary.")
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

