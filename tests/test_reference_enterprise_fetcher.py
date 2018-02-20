from unittest import TestCase

from brochure.value_fetchers.enterprise_fetcher_interface import EnterpriseFetcherInterface
from brochure_contract_tests.enterprise_fetcher_contract import EnterpriseFetcherContract
from brochure_reference_implementations.reference_enterprise_fetcher import ReferenceEnterpriseFetcher


class TestReferenceEnterpriseFetcher(TestCase, EnterpriseFetcherContract):
    def get_subject(self, name: str) -> EnterpriseFetcherInterface:
        return ReferenceEnterpriseFetcher(name=name)

    def get_testcase(self) -> TestCase:
        return self
