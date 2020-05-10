from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication


def first(request):
    books = Book.objects.all()
    return render(request, 'test.html', {'books': books})


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)


