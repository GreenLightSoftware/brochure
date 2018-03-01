from abc import ABCMeta, abstractmethod
from unittest import TestCase

from brochure.value_fetchers.contact_method_fetcher_interface import ContactMethodFetcherInterface
from brochure.values.contact_method import ContactMethodType


class ContactMethodFetcherContract(metaclass=ABCMeta):
    @abstractmethod
    def get_subject(self, contact_method_type: ContactMethodType, value: str) -> ContactMethodFetcherInterface:
        pass

    @abstractmethod
    def get_testcase(self) -> TestCase:
        pass

    def test_call_returns_contact_method_with_correct_email(self):
        subject = self.get_subject(contact_method_type=ContactMethodType.EMAIL, value="ejemplo@example.com")
        test_case = self.get_testcase()

        contact_method = subject()
        test_case.assertEqual(contact_method.contact_method_type, ContactMethodType.EMAIL)

    def test_call_returns_contact_method_with_correct_value(self):
        subject = self.get_subject(contact_method_type=ContactMethodType.EMAIL, value="ejemplo@example.com")
        test_case = self.get_testcase()

        contact_method = subject()
        test_case.assertEqual(contact_method.value, "ejemplo@example.com")
