from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that username already exists.",
            )
        ]
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
            )
        ]
    )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)
            if key == "password":
                instance.set_password(value)

        instance.save()

        return instance

    class Meta:
        model = User
        fields = ["id","password","full_name","artistic_name","username", "email"]
        extra_kwargs = {"password": {"write_only": True}}
        required_fields = ["username", "email"]
