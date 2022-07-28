from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework import response, generics
from accounts.models import Account, Transaction, TransactionTag
from accounts.serializers import AccountSerializer, TransactionSerializer, TransactionTagSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return Account.objects.filter(owner=user.id)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['get'])
    def transactions(self, request, pk=None):
        transactions = Transaction.objects.filter(account__id=pk)
        serializer = TransactionSerializer(transactions, many=True)
        return response.Response(serializer.data)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        queryset = Transaction.objects.filter(account__owner=user.id)
        tags = self.request.query_params.get('tags')
        if tags is not None:
            queryset = queryset.filter(tags_id=tags)
        return queryset


class TransactionTagViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionTagSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return TransactionTag.objects.filter(owner=user.id)


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
