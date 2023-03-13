from users.serializers.register import RegisterSerializer
from users.models import User
from rest_framework import generics


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer