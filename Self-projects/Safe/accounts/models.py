from django.utils import timezone
from django.db import models
from datetime import datetime

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=60)
    balance = models.FloatField(default = 0.00)
    
    def get_transactions(self):
        transactions = Transaction.objects.filter(account_id = self.id)
        return transactions
    
    
    def get_balance(self, startDate=datetime.min, endDate= datetime.max):
        transactions = Transaction.objects.filter(date__range = [startDate, endDate]).filter(account_id = self.id)
        temp_balance = self.balance
        for transaction in transactions: 
            if transaction.type =="DB":
                temp_balance -= transaction.amount
            else:
                temp_balance += transaction.amount
        return temp_balance


    def __str__(self):
           return f'{self.name}: ' + "{:.2f}".format(self.balance)

def get_or_create_default_acc():
    default_pk, _ = Account.objects.get_or_create(id=1)
    return default_pk


class TransactionTag(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=5, choices=[("CR", "Income"), ("DB", "Expense")], default="CR")

    def __str__(self):
        return f'({self.type}) {self.name}'


class Transaction(models.Model):
    name = models.CharField(max_length=60)
    type = models.CharField(max_length=5, choices=[("CR", "Income"), ("DB", "Expense")], default="CR")
    amount = models.FloatField(default = 0.00)
    date = models.DateField(default = timezone.now)
    tags = models.ForeignKey(TransactionTag, default=None, on_delete=models.SET_DEFAULT)
    account = models.ForeignKey(Account, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.type}) {self.name} ' + "{:.2f}".format(self.amount)

