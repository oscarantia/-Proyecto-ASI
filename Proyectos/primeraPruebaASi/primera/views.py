from django.http import HttpResponse
#api rest imports

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from primera.serializers import UserSerializer, GroupSerializer

#api rest

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def index(request):
    return HttpResponse("Hello, world. Estas en ASI.")

