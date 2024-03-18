from enum import Enum

class MembershipType(Enum):
    BASIC = 'Basic'
    PREMIUM = 'Premium'
    GOLD = 'Gold'

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]