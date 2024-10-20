import argparse
import json
import logging
from deebee.core import CollectionManager, DocumentStore, QueryEngine

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description="NoSQL Database Management CLI")
    subparsers = parser.add_subparsers(dest='command')

    # Create collection
    create_parser = subparsers.add_parser('create', help='Create a new collection')
    create_parser.add_argument('name', type=str, help='Name of the collection')

    # Insert document
    insert_parser = subparsers.add_parser('insert', help='Insert a document into a collection')
    insert_parser.add_argument('collection', type=str, help='Collection name')
    insert_parser.add_argument('document', type=str, help='Document to insert (JSON format)')

    # Query documents
    query_parser = subparsers.add_parser('query', help='Query documents in a collection')
    query_parser.add_argument('collection', type=str, help='Collection name')
    query_parser.add_argument('query', type=str, help='Query conditions (JSON format)')

    # List collections
    subparsers.add_parser('list', help='List all collections')

    args = parser.parse_args()

    try:
        if args.command == 'create':
            collection_manager = CollectionManager()
            collection_manager.create_collection(args.name)
            logging.info(f"Collection '{args.name}' created.")

        elif args.command == 'insert':
            document_store = DocumentStore(args.collection)
            try:
                document = json.loads(args.document)
                document_store.insert(document)
                logging.info(f"Document inserted into '{args.collection}': {json.dumps(document, indent=2)}")
            except json.JSONDecodeError:
                logging.error("Invalid JSON format. Please provide a valid JSON document.")

        elif args.command == 'query':
            document_store = DocumentStore(args.collection)
            try:
                query_conditions = json.loads(args.query)
                query_result = QueryEngine.query(document_store.documents, query_conditions)
                logging.info("Query result:\n%s", json.dumps(query_result, indent=2))
            except json.JSONDecodeError:
                logging.error("Invalid JSON format for query conditions.")

        elif args.command == 'list':
            collection_manager = CollectionManager()
            collections = collection_manager.list_collections()
            if collections:
                logging.info("Available collections: %s", ', '.join(collections))
            else:
                logging.info("No collections found.")

        else:
            parser.print_help()

    except Exception as e:
        logging.error("An error occurred: %s", str(e))

if __name__ == "__main__":
    main()
