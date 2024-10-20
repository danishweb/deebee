from flask import Flask, request, jsonify
from deebee.core.collection_manager import CollectionManager
from deebee.core.document_store import DocumentStore
from deebee.core.query_engine import QueryEngine
from deebee.core.schema_manager import SchemaManager

app = Flask(__name__)

# Initialize managers
collection_manager = CollectionManager()
schema_manager = SchemaManager()

@app.route('/collections', methods=['POST'])
def create_collection():
    data = request.json
    collection_name = data.get('name')
    schema = data.get('schema')

    if not collection_name:
        return jsonify({"error": "Collection name is required."}), 400

    # Create the collection
    collection_manager.create_collection(collection_name)

    # Define the schema for the collection (optional)
    if schema:
        schema_manager.define_schema(collection_name, schema)

    return jsonify({"message": f"Collection '{collection_name}' created.", "schema": schema}), 201

@app.route('/collections/<collection_name>/documents', methods=['POST'])
def insert_document(collection_name):
    document_store = DocumentStore(collection_name)
    document = request.json
    print(schema_manager.schemas.get(collection_name) is not None)
    if schema_manager.schemas.get(collection_name) is not None:
    # Validate the document against the schema
        try:
            schema_manager.validate(collection_name, document)
        except ValueError as e:
            return jsonify({"error": str(e)}),

    # Insert the validated document
    document_store.insert(document)
    return jsonify({"message": "Document inserted.", "document": document}), 201

@app.route('/collections/<collection_name>/documents', methods=['GET'])
def query_documents(collection_name):
    document_store = DocumentStore(collection_name)

    documents = document_store.documents  # Load documents explicitly
    
    if not documents:
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
