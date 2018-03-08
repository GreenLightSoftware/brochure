from abc import ABCMeta, abstractmethod
from unittest import TestCase

from brochure.value_fetchers.section_repository_interface import SectionRepositoryInterface


class SectionRepositoryContract(metaclass=ABCMeta):
    @abstractmethod
    def get_subject(self) -> SectionRepositoryInterface:
        pass

    @abstractmethod
    def get_testcase(self) -> TestCase:
        pass

    def test_create_cover_section_makes_cover_section_title_fetchable(self):
        subject = self.get_subject()
        test_case = self.get_testcase()
        expected_fields = {"title": "My Special Cover Section",
                           "body": "Doesn't matter"}
        subject.create_cover_section(**expected_fields)
        cover_section = subject.fetch_cover_section()

        test_case.assertEqual(cover_section.title, "My Special Cover Section")

    def test_create_another_cover_section_makes_cover_section_title_fetchable(self):
        subject = self.get_subject()
        test_case = self.get_testcase()
        expected_fields = {"title": "My Other Cover Section",
                           "body": "Doesn't matter"}
        subject.create_cover_section(**expected_fields)
        cover_section = subject.fetch_cover_section()

        test_case.assertEqual(cover_section.title, "My Other Cover Section")

    def test_create_cover_section_makes_cover_section_body_fetchable(self):
        subject = self.get_subject()
        test_case = self.get_testcase()
        expected_fields = {"title": "Doesn't matter",
                           "body": "My Special Section Body"}
        subject.create_cover_section(**expected_fields)
        cover_section = subject.fetch_cover_section()
        test_case.assertEqual(cover_section.body, "My Special Section Body")

    def test_create_another_cover_section_makes_cover_section_body_fetchable(self):
        subject = self.get_subject()
        test_case = self.get_testcase()
        expected_fields = {"title": "Doesn't matter",
                           "body": "My Other Section Body"}
        subject.create_cover_section(**expected_fields)
        cover_section = subject.fetch_cover_section()
        test_case.assertEqual(cover_section.body, "My Other Section Body")

    def test_created_cover_section_should_have_no_parent_identifier(self):
        subject = self.get_subject()
        test_case = self.get_testcase()
        section_identifier = subject.create_cover_section(title="My Special Cover Section",
                                                          body="My Special Section Body")
        cover_section = subject.fetch_section(identifier=section_identifier)
        test_case.assertIsNone(cover_section.parent_section_identifier)

    def test_fetch_cover_section_returns_section_with_empty_parent_identifier(self):
        subject = self.get_subject()
        test_case = self.get_testcase()
        subject.create_cover_section(title="My Special Cover Section",
                                     body="My Special Section Body")
        cover_section = subject.fetch_cover_section()
        test_case.assertIsNone(cover_section.parent_section_identifier)

    def test_create_section_fetch_section_returns_section_with_title(self):
        subject = self.get_subject()
        test_case = self.get_testcase()

        cover_section_identifier = subject.create_cover_section(title="My Special Cover Section",
                                                                body="My Special Section Body")
        section_identifier = subject.create_section(title="My special sub section",
                                                    body="My special sub section body",
                                                    parent_section_identifier=cover_section_identifier)
        section = subject.fetch_section(identifier=section_identifier)
        test_case.assertEqual("My special sub section", section.title)
