from unittest import TestCase

from brochure.value_fetchers.contact_method_fetcher_interface import ContactMethodFetcherInterface
from brochure.values.contact_method import ContactMethodType
from brochure_contract_tests.contact_method_fetcher_contract import ContactMethodFetcherContract
from brochure_reference_implementations.reference_contact_method_fetcher import ReferenceContactMethodFetcher


class TestReferenceContactMethodFetcher(TestCase, ContactMethodFetcherContract):

    def get_subject(self, contact_method_type: ContactMethodType, value: str) -> ContactMethodFetcherInterface:
        return ReferenceContactMethodFetcher(contact_method_type=contact_method_type, value=value)

    def get_testcase(self) -> TestCase:
        return self
