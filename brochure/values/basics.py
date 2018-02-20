from typing import NamedTuple

from brochure.values.contact_method import ContactMethod
from brochure.values.enterprise import Enterprise


class Basics(NamedTuple):
    enterprise: Enterprise
    contact_method: ContactMethod
