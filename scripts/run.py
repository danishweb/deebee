from deebee.core import CollectionManager, DocumentStore, QueryEngine

def main():
    # Initialize the Collection Manager
    collection_manager = CollectionManager()

    # Create a new collection
    collection_name = "users"
    collection_manager.create_collection(collection_name)
    print(f"Collection '{collection_name}' created.")

    # Initialize the Document Store for the created collection
    document_store = DocumentStore(collection_name)

    # Insert documents into the collection
    document_store.insert({"name": "Alice", "age": 30})
    document_store.insert({"name": "Bob", "age": 25})
    print("Documents inserted.")

    # Query documents
    query_result = QueryEngine.query(document_store.documents, {"age": 30})
    print("Query result:", query_result)

    # List all collections
    collections = collection_manager.list_collections()
    print("Collections:", collections)

    # Delete a document by ID
    if query_result:
        document_id = query_result[0]['_id']
        document_store.delete(document_id)
        print(f"Document with ID '{document_id}' deleted.")

    # List documents after deletion
    print("Documents after deletion:", document_store.documents)

if __name__ == "__main__":
    main()