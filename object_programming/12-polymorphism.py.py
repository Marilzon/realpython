class Bank:
    bank_name = "global_bank"

    @staticmethod
    def fee():
        return None


class SPBank(Bank):
    @staticmethod
    def fee():
        return 0.1
