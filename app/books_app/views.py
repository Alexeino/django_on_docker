from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import BookSerializer
from .models import Books
# Create your views here.

class BooksView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Books.objects.all()