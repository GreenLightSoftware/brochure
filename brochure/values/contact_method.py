from enum import Enum
from typing import NamedTuple


class ContactMethodType(Enum):
    EMAIL = 1


class ContactMethod(NamedTuple):
    contact_method_type: ContactMethodType
    value: str
