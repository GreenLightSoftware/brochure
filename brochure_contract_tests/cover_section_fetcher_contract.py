from abc import ABCMeta, abstractmethod
from unittest import TestCase

from brochure.value_fetchers.cover_section_fetcher_interface import CoverSectionFetcherInterface
from brochure.values.section import Section


class CoverSectionFetcherContract(metaclass=ABCMeta):
    @abstractmethod
    def get_subject(self, title: str, body: str) -> CoverSectionFetcherInterface:
        pass

    @abstractmethod
    def get_testcase(self) -> TestCase:
        pass

    def test_call_returns_cover_section_title(self):
        subject = self.get_subject(title="My Special Cover Section",
                                   body="My Special Section Body")
        test_case = self.get_testcase()

        cover_section = subject()
        expected_cover_section = Section(title="My Special Cover Section",
                                         body="My Special Section Body")
        test_case.assertEqual(cover_section, expected_cover_section)
