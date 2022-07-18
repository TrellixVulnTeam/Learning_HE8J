from rest_framework import serializers

from .models import Account, Transaction, TransactionTag

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class TransactionTagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransactionTag
        fields = '__all__'