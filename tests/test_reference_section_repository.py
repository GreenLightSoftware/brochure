from unittest import TestCase

from brochure.value_fetchers.section_repository_interface import SectionRepositoryInterface
from brochure_contract_tests.section_repository_contract import SectionRepositoryContract
from brochure_reference_implementations.reference_section_repository import ReferenceSectionRepository


class TestReferenceSectionRepository(TestCase, SectionRepositoryContract):

    def get_subject(self) -> SectionRepositoryInterface:
        return ReferenceSectionRepository()

    def get_testcase(self) -> TestCase:
        return self
