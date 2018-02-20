from typing import Callable, Type

from brochure.values.contact_method import ContactMethod

ContactMethodFetcherInterface = Type[Callable[[], ContactMethod]]
