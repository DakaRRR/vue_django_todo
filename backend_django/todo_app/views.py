from rest_framework.viewsets import ModelViewSet

from .models import Todo
from .serializers import TodoSerializer


class TodosViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


