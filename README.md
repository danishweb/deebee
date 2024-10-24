# Deebee: JSON DB

## Overview

Deebee is a JSON Document Management System built using Flask, providing a RESTful API for managing collections of documents. It allows users to create collections, insert documents, query documents, and delete collections. The system includes schema validation to ensure that documents conform to predefined structures, enhancing data integrity. Deebee is packaged as a Python module, making it easy to integrate into other applications or use as a standalone tool.

## Features

- **Create Collections**: Users can create new collections with optional schemas.
- **Insert Documents**: Documents can be inserted into collections after validation against the defined schema.
- **Query Documents**: Users can retrieve documents based on query parameters.
- **Delete Collections**: Collections can be deleted when no longer needed.
- **Schema Management**: Define and validate schemas for collections to ensure data integrity.
- **Command-Line Interface (CLI)**: Deebee includes a CLI for managing collections and documents directly from the terminal, providing an alternative to the RESTful API.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **JSON**: Data interchange format used for storing collections and documents.
- **UUID**: Universally Unique Identifier for document identification.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/danishweb/deebee.git
   cd deebee
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Flask Application

1. Start the Flask application:
   ```bash
   python app.py
   ```
2. Use a tool like Postman or curl to interact with the API.

### Using the Command-Line Interface (CLI)

Deebee also provides a command-line interface for managing collections and documents. You can use the following commands:

- **Create Collection**:

  ```bash
  deebee create <collection_name>
  ```

- **Insert Document**:

  ```bash
  deebee insert <collection_name> '{"field_name": "value"}'
  ```

- **Query Documents**:

  ```bash
  deebee query <collection_name> '{"field_name": "value"}'
  ```

- **List Collections**:

  ```bash
  deebee list
  ```

- **Delete Collection**:
  ```bash
  deebee delete <collection_name>
  ```

### API Endpoints

- **Create Collection**: `POST /collections`
  - **Request Body**:
    ```json
    {
      "name": "collection_name",
      "schema": {
        "field_name": "field_type"
      }
    }
    ```
- **Insert Document**: `POST /collections/<collection_name>/documents`

  - **Request Body**:
    ```json
    {
      "field_name": "value"
    }
    ```

- **Query Documents**: `GET /collections/<collection_name>/documents`

  - **Query Parameters**: `?field_name=value`

- **List Collections**: `GET /collections`

- **Delete Collection**: `DELETE /collections/<collection_name>`

## Example

To create a collection with a schema, you would send a request to the **Create Collection** endpoint with the appropriate JSON body.

---
