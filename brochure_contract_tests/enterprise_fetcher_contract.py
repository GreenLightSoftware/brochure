from abc import ABCMeta, abstractmethod
from unittest import TestCase

from brochure.value_fetchers.enterprise_fetcher_interface import EnterpriseFetcherInterface


class EnterpriseFetcherContract(metaclass=ABCMeta):
    @abstractmethod
    def get_subject(self, name: str) -> EnterpriseFetcherInterface:
        pass

    @abstractmethod
    def get_testcase(self) -> TestCase:
        pass

    def test_fetch_returns_enterprise(self):
        subject = self.get_subject(name="Acme Inc.")
        test_case = self.get_testcase()

        enterprise = subject()
        test_case.assertEqual(enterprise.name, "Acme Inc.")
