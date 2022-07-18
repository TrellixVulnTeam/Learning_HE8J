from django.shortcuts import render
from rest_framework import viewsets

from accounts.models import Account, Transaction, TransactionTag
from accounts.serializers import AccountSerializer, TransactionSerializer, TransactionTagSerializer
# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionTagViewSet(viewsets.ModelViewSet):
    queryset = TransactionTag.objects.all()
    serializer_class = TransactionTagSerializer

