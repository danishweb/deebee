import os
import json
from datetime import datetime

class CollectionManager:
    def __init__(self, base_path: str='collections'):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)


    def create_collection(self, name: str):
        '''Create a new collection'''
        collection_path = os.path.join(self.base_path, f"{name}.json")
        if os.path.exists(collection_path):
            raise FileExistsError(f"Collection {name} already exists")
        with open(collection_path, "w") as f:
            json.dump({"name": name, "created_at": datetime.now().isoformat()}, f)


    def delete_collection(self, name: str):
        '''Delete a collection'''
        collection_path = os.path.join(self.base_path, f"{name}.json")
        if not os.path.exists(collection_path):
            raise FileNotFoundError(f"Collection {name} does not exist")
        os.remove(collection_path)

    def list_collections(self):
        '''List all collections'''
        return [f[:-5] for f in os.listdir(self.base_path) if f.endswith('.json')]

    def get_collection(self, name: str):
        '''Get a collection'''
        collection_path = os.path.join(self.base_path, f"{name}.json")
        if not os.path.exists(collection_path):
            raise FileNotFoundError(f"Collection {name} does not exist")
        with open(collection_path, "r") as f:
            return json.load(f)