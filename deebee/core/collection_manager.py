import os
from datetime import datetime
from .persistence_layer import PersistenceLayer
from deebee.config.settings import base_collection_folder

class CollectionManager:
    def __init__(self, base_path: str = base_collection_folder):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

    def create_collection(self, name: str):
        """Create a new collection."""
        collection_path = f"{self.base_path}/{name}.json"
        if os.path.exists(collection_path):
            raise FileExistsError(f"Collection '{name}' already exists.")
        
        data = []
        PersistenceLayer.write_json(collection_path, data)

    def delete_collection(self, name: str):
        """Delete a collection."""
        collection_path = f"{self.base_path}/{name}.json"
        if not os.path.exists(collection_path):
            raise FileNotFoundError(f"Collection '{name}' does not exist.")
        os.remove(collection_path)

    def list_collections(self):
        """List all collections."""
        return [f[:-5] for f in os.listdir(self.base_path) if f.endswith('.json')]

    def get_collection(self, name: str):
        """Get a collection."""
        collection_path = f"{self.base_path}/{name}.json"
        if not os.path.exists(collection_path):
            raise FileNotFoundError(f"Collection '{name}' does not exist.")
        return PersistenceLayer.read_json(collection_path)
