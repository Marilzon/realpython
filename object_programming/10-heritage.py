import datetime, time

class MaxBank:
    def __init__(self, country: str) -> None:
        self.country = country

    @property
    def bank_name(self) -> str:
        return f"MaxBANK - {self.country}"


class Transaction(MaxBank):
    def __init__(self, country: str, type: str) -> str:
        super().__init__(country)
        self.type = type

    def update_timestamp(self) -> None:
        self.timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    def execute_transaction(self) -> str:
        self.update_timestamp()
        return f"execute {self.type} transaction complete {self.timestamp}"


for value in range(0, 5):
    transaction_brazil = Transaction("brazil", "deposit")
    time.sleep(2)

    print(transaction_brazil.execute_transaction())
