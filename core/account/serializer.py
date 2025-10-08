from .models import UserInfo
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"
