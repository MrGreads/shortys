from django.shortcuts import redirect, render
from rest_framework import permissions, viewsets
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group

from django.views import View
from django.conf import settings
from django.db.models import F
from rest_framework.viewsets import GenericViewSet

from .models import Link
from .serializer import LinkSerializer, UserSerializer, GroupSerializer


class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ShortenerListAPIView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [permissions.IsAuthenticated]


class ShortenerCreateApiView(CreateAPIView):
    serializer_class = LinkSerializer


class ShortenerInfo(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        short = Link.objects.get(id=pk)
        serializer = LinkSerializer(short)
        return Response(serializer.data)


class Redirector(View):
    def get(self, request, shortener_link, *args, **kwargs):
        shortener_link = settings.HOST_URL + '/' + self.kwargs['shortener_link']
        redirect_link = Link.objects.filter(shortened_link=shortener_link).first().original_link
        Link.objects.filter(shortened_link=shortener_link).update(clicked=F('clicked') + 1)
        return redirect(redirect_link)
