import json
import os
import portalocker

class PersistenceLayer:
    @staticmethod
    def read_json(file_path: str):
        """Thread-safe read operation for JSON files."""
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    print(f"Warning: {file_path} contains invalid JSON.")
                    return []
        return []

    @staticmethod
    def write_json(file_path, data):
        
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Open the file in write mode and use portalocker to lock it.
        with portalocker.Lock(file_path, 'w', flags=portalocker.LOCK_EX) as f:
            json.dump(data, f, indent=4)
