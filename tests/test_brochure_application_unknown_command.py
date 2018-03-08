from brochure.commands.command_types import CommandType
from brochure.values.basics import Basics
from brochure.values.contact_method import ContactMethodType, ContactMethod
from brochure.values.enterprise import Enterprise
from brochure.values.section import Section
from brochure_reference_implementations.named_tuple_fetcher_provider import NamedTupleFetcherProvider
from tests.brochure_application_test_case import BrochureApplicationTestCase

ReferenceCoverSectionFetcher = NamedTupleFetcherProvider(named_tuple_type=Section)


class TestBrochureApplicationUnknownCommand(BrochureApplicationTestCase):

    def test_unknown_command_passes_still_shows_basics_to_the_user_interface(self):
        sections = [{"title": "Another sub section", "body": "This is a subsection"}]
        expected_enterprise = Enterprise(name="Example Enterprise")
        expected_contact_method = ContactMethod(contact_method_type=ContactMethodType.EMAIL, value="admin@example.com")
        subject, user_interface = self.get_subject(expected_enterprise=expected_enterprise,
                                                   expected_contact_method=expected_contact_method,
                                                   expected_cover_section_title="Cover Section Title",
                                                   expected_cover_section_body="Cover Section Body",
                                                   expected_sections=sections)

        subject.process_command(command_provider=lambda: (CommandType.UNKNOWN, {}))

        self.assertEqual(user_interface.unknown_basics, Basics(enterprise=Enterprise(name="Example Enterprise"),
                                                               contact_method=ContactMethod(
                                                                   contact_method_type=ContactMethodType.EMAIL,
                                                                   value="admin@example.com")))

    # noinspection PyTypeChecker
    def test_unrecognized_command_behaves_like_unknown_command(self):
        sections = [{"title": "Another sub section", "body": "This is a subsection"}]
        expected_enterprise = Enterprise(name="Example Enterprise")
        expected_contact_method = ContactMethod(contact_method_type=ContactMethodType.EMAIL, value="admin@example.com")
        subject, user_interface = self.get_subject(expected_enterprise=expected_enterprise,
                                                   expected_contact_method=expected_contact_method,
                                                   expected_cover_section_title="Cover Section Title",
                                                   expected_cover_section_body="Cover Section Body",
                                                   expected_sections=sections)

        subject.process_command(command_provider=lambda: (-1, {}))

        self.assertEqual(user_interface.unknown_basics, Basics(enterprise=Enterprise(name="Example Enterprise"),
                                                               contact_method=ContactMethod(
                                                                   contact_method_type=ContactMethodType.EMAIL,
                                                                   value="admin@example.com")))
