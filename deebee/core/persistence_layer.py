import json
import os

class PersistenceLayer:
    @staticmethod
    def read_json(file_path):
        """Read JSON data from a file."""
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return json.load(f)
        return []

    @staticmethod
    def write_json(file_path, data):
        """Write JSON data to a file."""
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)