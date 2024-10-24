from django.http import JsonResponse
from django.views import View
from .models import Todo
from deebee.core.document_store import DocumentStore
import json
from django.shortcuts import render

# Initialize the DocumentStore for todos
document_store = DocumentStore("todos", 'data')

class HomePageView(View):
    def get(self, request):
        return render(request, 'todo/home.html')
    
class TodoListView(View):
    def get(self, request):
        # Retrieve all todos
        todos = document_store.documents
        return JsonResponse(todos, safe=False)

    def post(self, request):
        # Insert a new todo
        data = json.loads(request.body)
        document_store.insert(data)
        return JsonResponse({"message": "Todo added successfully!"}, status=201)
  

class TodoDetailView(View):
    def get(self, request, todo_id):
        # Retrieve a specific todo
        todos = document_store.documents
        todo = next((item for item in todos if item.get('_id') == todo_id), None)
        if todo:
            return JsonResponse(todo)
        return JsonResponse({"error": "Todo not found"}, status=404)

    def delete(self, request, todo_id):
        # Delete a specific todo
        todos = document_store.documents
        document_store.delete(todo_id)
        return JsonResponse({"message": "Todo deleted successfully!"}, status=204)