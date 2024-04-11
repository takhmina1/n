from rest_framework import serializers
from .models import Account, Transaction, Application


class AccountSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Account"""

    class Meta:
        model = Account
        fields = ['id', 'user', 'currency', 'balance']


class TransactionSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Transaction"""

    class Meta:
        model = Transaction
        fields = ['id', 'account', 'amount', 'transaction_type', 'timestamp', 'description']


class ApplicationSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Application"""

    class Meta:
        model = Application
        fields = ['id', 'account', 'currency', 'payment_id', 'amount', 'type', 'status']
