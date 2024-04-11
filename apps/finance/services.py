from .models import Account, Transaction, Application

class AccountService:
    @staticmethod
    def get_account_balance(account_id):
        """Получить баланс счета"""
        try:
            account = Account.objects.get(pk=account_id)
            return account.balance
        except Account.DoesNotExist:
            return None

    @staticmethod
    def deposit(account_id, amount):
        """Пополнить счет"""
        try:
            account = Account.objects.get(pk=account_id)
            account.balance += amount
            account.save()
            Transaction.objects.create(
                account=account,
                amount=amount,
                transaction_type=Transaction.DEPOSIT
            )
            return True
        except Account.DoesNotExist:
            return False

    @staticmethod
    def withdraw(account_id, amount):
        """Вывести средства со счета"""
        try:
            account = Account.objects.get(pk=account_id)
            if account.balance >= amount:
                account.balance -= amount
                account.save()
                Transaction.objects.create(
                    account=account,
                    amount=amount,
                    transaction_type=Transaction.WITHDRAWAL
                )
                return True
            return False
        except Account.DoesNotExist:
            return False

    @staticmethod
    def create_application(account_id, currency_id, amount, application_type):
        """Создать заявку на ввод/вывод средств"""
        try:
            account = Account.objects.get(pk=account_id)
            currency = Currency.objects.get(pk=currency_id)
            application = Application.objects.create(
                account=account,
                currency=currency,
                amount=amount,
                type=application_type,
                status=Application.PENDING
            )
            return application
        except (Account.DoesNotExist, Currency.DoesNotExist):
            return None


















































































































# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from .services import get_account_balance, deposit, withdraw, get_transaction_history

# class AccountBalanceView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         balance = get_account_balance(request.user)
#         if balance is not None:
#             return Response({'balance': balance}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

# class DepositView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def post(self, request):
#         amount = request.data.get('amount')
#         if amount:
#             response = deposit(request.user, amount)
#             if response['success']:
#                 return Response({'message': response['message']}, status=status.HTTP_201_CREATED)
#             else:
#                 return Response({'error': response['error']}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({'error': 'Amount not provided'}, status=status.HTTP_400_BAD_REQUEST)

# class WithdrawalView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def post(self, request):
#         amount = request.data.get('amount')
#         if amount:
#             response = withdraw(request.user, amount)
#             if response['success']:
#                 return Response({'message': response['message']}, status=status.HTTP_201_CREATED)
#             else:
#                 return Response({'error': response['error']}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({'error': 'Amount not provided'}, status=status.HTTP_400_BAD_REQUEST)

# class TransactionHistoryView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         response = get_transaction_history(request.user)
#         if response['success']:
#             return Response({'transactions': response['transactions']}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': response['error']}, status=status.HTTP_400_BAD_REQUEST)
