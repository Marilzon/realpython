from abc import ABC, abstractmethod


# abstract classes should not be instalce object, only hericantes.
class Bank(ABC):
    def create_agency(self):
        print("creating agency")

    @abstractmethod  # consumer class should have a process_payment method.
    def process_payments(self): ...


class BrazilBank(Bank):
    def process_payments(self):
        print("processing payments")


brazil_bank = BrazilBank()
brazil_bank.create_agency()
brazil_bank.process_payments()
