from typing import Callable

from brochure.values.basics import Basics
from brochure.values.contact_method import ContactMethod
from brochure.values.enterprise import Enterprise


class BasicsFetcher(object):

    def __init__(self,
                 contact_methods_fetcher: Callable[[], ContactMethod],
                 enterprise_fetcher: Callable[[], Enterprise]) -> None:
        super().__init__()
        self._contact_method_fetcher = contact_methods_fetcher
        self._enterprise_fetcher = enterprise_fetcher

    def __call__(self, *args, **kwargs) -> Basics:
        enterprise = self._enterprise_fetcher()
        contact_method = self._contact_method_fetcher()

        return Basics(enterprise=enterprise, contact_method=contact_method)
