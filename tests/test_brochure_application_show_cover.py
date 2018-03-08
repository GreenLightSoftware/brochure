from brochure.commands.command_types import CommandType
from brochure.values.basics import Basics
from brochure.values.contact_method import ContactMethodType, ContactMethod
from brochure.values.enterprise import Enterprise
from brochure.values.section import Section
from brochure_reference_implementations.named_tuple_fetcher_provider import NamedTupleFetcherProvider
from tests.brochure_application_test_case import BrochureApplicationTestCase

ReferenceCoverSectionFetcher = NamedTupleFetcherProvider(named_tuple_type=Section)


class TestBrochureApplicationShowCover(BrochureApplicationTestCase):

    def test_show_cover_shows_basics_to_the_user_interface(self):
        expected_enterprise = Enterprise(name="Example Enterprise")
        expected_contact_method = ContactMethod(contact_method_type=ContactMethodType.EMAIL,
                                                value="admin@example.com")
        subject, user_interface = self.get_subject(expected_enterprise=expected_enterprise,
                                                   expected_contact_method=expected_contact_method,
                                                   expected_cover_section_title="Cover Section",
                                                   expected_cover_section_body="Cover Section Body",
                                                   expected_sections=[])

        subject.process_command(command_provider=lambda: (CommandType.SHOW_COVER, {}))

        self.assertEqual(user_interface.basics, Basics(enterprise=Enterprise(name="Example Enterprise"),
                                                       contact_method=ContactMethod(
                                                           contact_method_type=ContactMethodType.EMAIL,
                                                           value="admin@example.com")))

    def test_show_cover_shows_section_title_to_the_user_interface(self):
        expected_enterprise = Enterprise(name="Example Enterprise")
        expected_contact_method = ContactMethod(contact_method_type=ContactMethodType.EMAIL,
                                                value="admin@example.com")
        subject, user_interface = self.get_subject(expected_enterprise=expected_enterprise,
                                                   expected_contact_method=expected_contact_method,
                                                   expected_cover_section_title="Cover Section",
                                                   expected_cover_section_body="Cover Section Body",
                                                   expected_sections=[])

        subject.process_command(command_provider=lambda: (CommandType.SHOW_COVER, {}))

        self.assertEqual(user_interface.cover_section.title, "Cover Section")

    def test_show_cover_shows_section_body_to_the_user_interface(self):
        expected_enterprise = Enterprise(name="Example Enterprise")
        expected_contact_method = ContactMethod(contact_method_type=ContactMethodType.EMAIL,
                                                value="admin@example.com")
        subject, user_interface = self.get_subject(expected_enterprise=expected_enterprise,
                                                   expected_contact_method=expected_contact_method,
                                                   expected_cover_section_title="Cover Section",
                                                   expected_cover_section_body="Cover Section Body",
                                                   expected_sections=[])

        subject.process_command(command_provider=lambda: (CommandType.SHOW_COVER, {}))

        self.assertEqual(user_interface.cover_section.body, "Cover Section Body")

    def test_show_cover_shows_another_cover_section_to_the_user_interface(self):
        expected_enterprise = Enterprise(name="Example Enterprise")
        expected_contact_method = ContactMethod(contact_method_type=ContactMethodType.EMAIL,
                                                value="admin@example.com")
        subject, user_interface = self.get_subject(expected_enterprise=expected_enterprise,
                                                   expected_contact_method=expected_contact_method,
                                                   expected_cover_section_title="Another Cover Section",
                                                   expected_cover_section_body="Cover Section Body",
                                                   expected_sections=[])

        subject.process_command(command_provider=lambda: (CommandType.SHOW_COVER, {}))

        self.assertEqual(user_interface.cover_section.title, "Another Cover Section")
