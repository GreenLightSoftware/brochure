from brochure.commands.command_types import CommandType
from brochure.values.basics import Basics
from brochure.values.contact_method import ContactMethodType, ContactMethod
from brochure.values.enterprise import Enterprise
from brochure.values.section import Section
from brochure_reference_implementations.named_tuple_fetcher_provider import NamedTupleFetcherProvider
from tests.brochure_application_test_case import BrochureApplicationTestCase

SectionFetcher = NamedTupleFetcherProvider(named_tuple_type=Section)


class TestBrochureApplicationShowSection(BrochureApplicationTestCase):

    def test_show_section_shows_basics_to_the_user_interface(self):
        sections = [{"title": "A sub section", "body": "This is a subsection"}]
        expected_enterprise = Enterprise(name="Example Enterprise")
        expected_contact_method = ContactMethod(contact_method_type=ContactMethodType.EMAIL, value="admin@example.com")
        subject, user_interface = self.get_subject(expected_enterprise=expected_enterprise,
                                                   expected_contact_method=expected_contact_method,
                                                   expected_cover_section_title="Cover Section Title",
                                                   expected_cover_section_body="Cover Section Body",
                                                   expected_sections=sections)

        subject.process_command(command_provider=lambda: (CommandType.SHOW_SECTION, {"identifier": 2}))

        expected_basics = Basics(enterprise=Enterprise(name="Example Enterprise"),
                                 contact_method=ContactMethod(contact_method_type=ContactMethodType.EMAIL,
                                                              value="admin@example.com"))
        self.assertEqual(expected_basics, user_interface.basics)

    def test_show_section_shows_section_title_to_the_user_interface(self):
        sections = [{"title": "A sub section", "body": "This is a subsection"}]
        expected_enterprise = Enterprise(name="Example Enterprise")
        expected_contact_method = ContactMethod(contact_method_type=ContactMethodType.EMAIL, value="admin@example.com")
        subject, user_interface = self.get_subject(expected_enterprise=expected_enterprise,
                                                   expected_contact_method=expected_contact_method,
                                                   expected_cover_section_title="Cover Section Title",
                                                   expected_cover_section_body="Cover Section Body",
                                                   expected_sections=sections)

        subject.process_command(command_provider=lambda: (CommandType.SHOW_SECTION, {"identifier": 2}))

        self.assertEqual(user_interface.section.title, "A sub section")

    def test_show_section_shows_section_body_to_the_user_interface(self):
        sections = [{"title": "A sub section", "body": "This is a subsection"}]
        expected_enterprise = Enterprise(name="Example Enterprise")
        expected_contact_method = ContactMethod(contact_method_type=ContactMethodType.EMAIL, value="admin@example.com")
        subject, user_interface = self.get_subject(expected_enterprise=expected_enterprise,
                                                   expected_contact_method=expected_contact_method,
                                                   expected_cover_section_title="Cover Section Title",
                                                   expected_cover_section_body="Cover Section Body",
                                                   expected_sections=sections)

        subject.process_command(command_provider=lambda: (CommandType.SHOW_SECTION, {"identifier": 2}))

        self.assertEqual(user_interface.section.body, "This is a subsection")

    def test_show_section_shows_another_section_title_to_the_user_interface(self):
        sections = [{"title": "Another sub section", "body": "This is a subsection"}]
        expected_enterprise = Enterprise(name="Example Enterprise")
        expected_contact_method = ContactMethod(contact_method_type=ContactMethodType.EMAIL, value="admin@example.com")
        subject, user_interface = self.get_subject(expected_enterprise=expected_enterprise,
                                                   expected_contact_method=expected_contact_method,
                                                   expected_cover_section_title="Cover Section Title",
                                                   expected_cover_section_body="Cover Section Body",
                                                   expected_sections=sections)

        subject.process_command(command_provider=lambda: (CommandType.SHOW_SECTION, {"identifier": 2}))

        self.assertEqual(user_interface.section.title, "Another sub section")
