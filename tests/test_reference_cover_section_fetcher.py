from unittest import TestCase

from brochure.value_fetchers.cover_section_fetcher_interface import CoverSectionFetcherInterface
from brochure_contract_tests.cover_section_fetcher_contract import CoverSectionFetcherContract
from tests.test_brochure_application import ReferenceCoverSectionFetcher


class TestReferenceCoverSectionFetcher(TestCase, CoverSectionFetcherContract):
    def get_subject(self, title: str, body: str) -> CoverSectionFetcherInterface:
        return ReferenceCoverSectionFetcher(title=title, body=body)

    def get_testcase(self) -> TestCase:
        return self
