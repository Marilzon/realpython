 # BAD OPEN CLOSED SOLID
class Transaction:
    def execute(self, transaction_type: str) -> None:
        if transaction_type == "credit":
            return self.__execute_credit()
        if transaction_type == "debit":
            return self.__execute_debit()

    def __execute_credit(self):
        return f"Credit operation success."

    def __execute_debit(self):
        return f"Debit operation success."

transaction = Transaction()
operation = "credit"
print(transaction.execute(operation)+"\n")

# NICE OPEN CLOSED SOLID
class Account:
    def __init__(self, account_type: str) -> None:
        self.account_type = account_type

    def account_description(self) -> None:
        return f"account_description: {self.account_type}"


invest_account = "invest_account"
account_a = Account(invest_account)
salary_account = "salary_account"
account_b = Account(salary_account)

print(account_a.account_description())
print(account_b.account_description())
