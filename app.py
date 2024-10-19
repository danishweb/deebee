from flask import Flask, request, jsonify
from deebee.core.collection_manager import CollectionManager
from deebee.core.document_store import DocumentStore
from deebee.core.query_engine import QueryEngine

app = Flask(__name__)

# Initialize the Collection Manager
collection_manager = CollectionManager()

@app.route('/collections', methods=['POST'])
def create_collection():
    data = request.json
    collection_name = data.get('name')
    if not collection_name:
        return jsonify({"error": "Collection name is required."}), 400
    collection_manager.create_collection(collection_name)
    return jsonify({"message": f"Collection '{collection_name}' created."}), 201

@app.route('/collections/<collection_name>/documents', methods=['POST'])
def insert_document(collection_name):
    document_store = DocumentStore(collection_name)
    document = request.json
    document_store.insert(document)
    return jsonify({"message": "Document inserted.", "document": document}), 201

@app.route('/collections/<collection_name>/documents', methods=['GET'])
def query_documents(collection_name):
    document_store = DocumentStore(collection_name)

    # Ensure documents are properly loaded
    documents = document_store.documents  # Load documents explicitly
    
    if documents is None:
        return jsonify({"error": "Collection not found or empty."}), 404

    # Convert query parameters into expected types (e.g., age as integer)
    query_params = {k: try_parse_int(v) for k, v in request.args.items()}

    # Perform the query
    query_result = QueryEngine.query(documents, query_params)
    return jsonify(query_result), 200

@app.route('/collections', methods=['GET'])
def list_collections():
    collections = collection_manager.list_collections()
    return jsonify(collections), 200

def try_parse_int(value):
    """Helper function to convert string to int if possible."""
    try:
        return int(value)
    except ValueError:
        return value

if __name__ == '__main__':
    app.run(port=5000, debug=True)
