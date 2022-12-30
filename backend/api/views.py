from http import HTTPStatus

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from users.models import User
from .filters import IngredientSearchFilter, RecipeFilters
from .serializers import (UserSerializer,
)

class CreateUserView(UserViewSet):
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.all()
    