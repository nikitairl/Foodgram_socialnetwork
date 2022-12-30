from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from ..recipes.models import (
    Subscribe
)
from ..users.models import User


class SubscribeChecker(metaclass=serializers.SerializerMetaclass):
    """
    Сериализатор подписки на авторов
    """
    is_subscribed = serializers.SerializerMethodField

    def sub_check(self,obj):
        request = self.context.get('request')
        if request.user.is_anonymous:
            return False
        if Subscribe.objects.filter(
            user=request.user, following_id=obj.id).exists():
            return True
        else:
            return False



class UserSerializer():
    """
    Сериализатор модели пользователя
    """
    class Meta:
        model = User
        fields = ('__all__')
        write_only_fields = ('password')
        read_only_fields = ('id')
        extra_kwargs = {'is_subscribed': {'required':False}}

    def to_representation(self,obj):
        """
        Метод представления результатов сериализатора
        """
        result = super(UserSerializer, self).to_representation(obj)
        result.pop('password', None)
        return result