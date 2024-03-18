from enum import Enum

class PaymentStatusType(Enum):
    Pending = 'Pending'
    Payment_done = 'Payment_successful'
    

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]