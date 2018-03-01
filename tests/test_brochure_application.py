from typing import Tuple, Dict
from unittest import TestCase

from brochure.brochure_application import BrochureApplication
from brochure.commands.command_types import CommandType
from brochure.values.basics import Basics
from brochure.values.contact_method import ContactMethodType, ContactMethod
from brochure.values.enterprise import Enterprise
from brochure.values.section import Section
from brochure_reference_implementations.named_tuple_fetcher_provider import NamedTupleFetcherProvider
from brochure_reference_implementations.reference_contact_method_fetcher import ReferenceContactMethodFetcher
from brochure_reference_implementations.reference_enterprise_fetcher import ReferenceEnterpriseFetcher
from brochure_reference_implementations.reference_user_interface import ReferenceUserInterface

ReferenceCoverSectionFetcher = NamedTupleFetcherProvider(named_tuple_type=Section)


class TestBrochureApplication(TestCase):
    @staticmethod
    def get_subject(expected_enterprise: Enterprise,
                    expected_contact_method: ContactMethod,
                    expected_cover_section: Section) -> Tuple[BrochureApplication, ReferenceUserInterface]:
        cover_section_fetcher = ReferenceCoverSectionFetcher(**expected_cover_section._asdict())
        contact_method_fetcher = ReferenceContactMethodFetcher(**expected_contact_method._asdict())
        enterprise_fetcher = ReferenceEnterpriseFetcher(**expected_enterprise._asdict())
        user_interface = ReferenceUserInterface()
        application = BrochureApplication(contact_method_fetcher=contact_method_fetcher,
                                          cover_section_fetcher=cover_section_fetcher,
                                          enterprise_fetcher=enterprise_fetcher)
        application.register_user_interface(user_interface=user_interface)

        return application, user_interface

    def test_show_cover_shows_basics_to_the_user_interface(self):
        expected_cover_section = Section(title="Cover Section", body="Cover Section Body")
        expected_enterprise = Enterprise(name="Example Enterprise")
        expected_contact_method = ContactMethod(contact_method_type=ContactMethodType.EMAIL,
                                                value="admin@example.com")
        subject, user_interface = self.get_subject(expected_enterprise=expected_enterprise,
                                                   expected_contact_method=expected_contact_method,
                                                   expected_cover_section=expected_cover_section)

        subject.process_command(command_provider=lambda: (CommandType.SHOW_COVER, {}))

        self.assertEqual(user_interface.basics, Basics(enterprise=Enterprise(name="Example Enterprise"),
                                                       contact_method=ContactMethod(
                                                           contact_method_type=ContactMethodType.EMAIL,
                                                           value="admin@example.com")))

    def test_show_cover_shows_section_title_to_the_user_interface(self):
        expected_cover_section = Section(title="Cover Section", body="Cover Section Body")
        expected_enterprise = Enterprise(name="Example Enterprise")
        expected_contact_method = ContactMethod(contact_method_type=ContactMethodType.EMAIL,
                                                value="admin@example.com")
        subject, user_interface = self.get_subject(expected_enterprise=expected_enterprise,
                                                   expected_contact_method=expected_contact_method,
                                                   expected_cover_section=expected_cover_section)

        subject.process_command(command_provider=lambda: (CommandType.SHOW_COVER, {}))

        self.assertEqual(user_interface.cover_section.title, "Cover Section")

    def test_show_cover_shows_section_body_to_the_user_interface(self):
        expected_cover_section = Section(title="Cover Section", body="Cover Section Body")
        expected_enterprise = Enterprise(name="Example Enterprise")
        expected_contact_method = ContactMethod(contact_method_type=ContactMethodType.EMAIL,
                                                value="admin@example.com")
        subject, user_interface = self.get_subject(expected_enterprise=expected_enterprise,
                                                   expected_contact_method=expected_contact_method,
                                                   expected_cover_section=expected_cover_section)

        subject.process_command(command_provider=lambda: (CommandType.SHOW_COVER, {}))

        self.assertEqual(user_interface.cover_section.body, "Cover Section Body")

    def test_show_cover_shows_another_cover_section_to_the_user_interface(self):
        expected_cover_section = Section(title="Another Cover Section", body="Cover Section Body")
        expected_enterprise = Enterprise(name="Example Enterprise")
        expected_contact_method = ContactMethod(contact_method_type=ContactMethodType.EMAIL,
                                                value="admin@example.com")
        subject, user_interface = self.get_subject(expected_enterprise=expected_enterprise,
                                                   expected_contact_method=expected_contact_method,
                                                   expected_cover_section=expected_cover_section)

        subject.process_command(command_provider=lambda: (CommandType.SHOW_COVER, {}))

        self.assertEqual(user_interface.cover_section.title, "Another Cover Section")

    def test_unknown_command_passes_still_shows_basics_to_the_user_interface(self):
        expected_cover_section = Section(title="Cover Section", body="Cover Section Body")
        expected_enterprise = Enterprise(name="Example Enterprise")
        expected_contact_method = ContactMethod(contact_method_type=ContactMethodType.EMAIL,
                                                value="admin@example.com")
        subject, user_interface = self.get_subject(expected_enterprise=expected_enterprise,
                                                   expected_contact_method=expected_contact_method,
                                                   expected_cover_section=expected_cover_section)

        subject.process_command(command_provider=lambda: (CommandType.UNKNOWN, {}))

        self.assertEqual(user_interface.unknown_basics, Basics(enterprise=Enterprise(name="Example Enterprise"),
                                                               contact_method=ContactMethod(
                                                                   contact_method_type=ContactMethodType.EMAIL,
                                                                   value="admin@example.com")))

    # noinspection PyTypeChecker
    def test_unrecognized_command_passes_still_shows_basics_to_the_user_interface(self):
        expected_cover_section = Section(title="Cover Section", body="Cover Section Body")
        expected_enterprise = Enterprise(name="Example Enterprise")
        expected_contact_method = ContactMethod(contact_method_type=ContactMethodType.EMAIL,
                                                value="admin@example.com")
        subject, user_interface = self.get_subject(expected_enterprise=expected_enterprise,
                                                   expected_contact_method=expected_contact_method,
                                                   expected_cover_section=expected_cover_section)

        subject.process_command(command_provider=lambda: (-1, {}))

        self.assertEqual(user_interface.unknown_basics, Basics(enterprise=Enterprise(name="Example Enterprise"),
                                                               contact_method=ContactMethod(
                                                                   contact_method_type=ContactMethodType.EMAIL,
                                                                   value="admin@example.com")))

    def test_raising_exception_still_tries_to_show_basics_to_the_user_interface(self):
        expected_cover_section = Section(title="Cover Section", body="Cover Section Body")
        expected_enterprise = Enterprise(name="Example Enterprise")
        expected_contact_method = ContactMethod(contact_method_type=ContactMethodType.EMAIL,
                                                value="admin@example.com")
        subject, user_interface = self.get_subject(expected_enterprise=expected_enterprise,
                                                   expected_contact_method=expected_contact_method,
                                                   expected_cover_section=expected_cover_section)

        # noinspection PyUnreachableCode
        def dummy() -> Tuple[CommandType, Dict]:
            raise Exception()
            return CommandType.SHOW_COVER, {}

        subject.process_command(command_provider=dummy)

        self.assertEqual(user_interface.exception_basics, Basics(enterprise=Enterprise(name="Example Enterprise"),
                                                                 contact_method=ContactMethod(
                                                                     contact_method_type=ContactMethodType.EMAIL,
                                                                     value="admin@example.com")))

    def test_raising_exception_shows_exception_to_the_user_interface(self):
        expected_cover_section = Section(title="Cover Section", body="Cover Section Body")
        expected_enterprise = Enterprise(name="Example Enterprise")
        expected_contact_method = ContactMethod(contact_method_type=ContactMethodType.EMAIL,
                                                value="admin@example.com")
        subject, user_interface = self.get_subject(expected_enterprise=expected_enterprise,
                                                   expected_contact_method=expected_contact_method,
                                                   expected_cover_section=expected_cover_section)

        class MySpecialException(Exception):
            pass

        # noinspection PyUnreachableCode
        def dummy() -> Tuple[CommandType, Dict]:
            raise MySpecialException()
            return CommandType.SHOW_COVER, {}

        subject.process_command(command_provider=dummy)

        self.assertEqual(type(user_interface.exception), MySpecialException)

    def test_raising_exception_shows_exception_to_the_user_interface_even_if_basics_cant_be_shown(self):
        class MyContactMethodFetcherException(Exception):
            pass

        def contact_method_fetcher() -> ContactMethod:
            raise MyContactMethodFetcherException()
            # noinspection PyUnreachableCode
            return ContactMethod(contact_method_type=ContactMethodType.EMAIL, value="admin@example.com")

        cover_section_fetcher = ReferenceCoverSectionFetcher({"title": "Cover Section"})
        enterprise_fetcher = ReferenceEnterpriseFetcher({"name": "Example Enterprise"})
        user_interface = ReferenceUserInterface()
        application = BrochureApplication(contact_method_fetcher=contact_method_fetcher,
                                          cover_section_fetcher=cover_section_fetcher,
                                          enterprise_fetcher=enterprise_fetcher)
        application.register_user_interface(user_interface=user_interface)

        class MyCommandProviderException(Exception):
            pass

        # noinspection PyUnreachableCode
        def dummy() -> Tuple[CommandType, Dict]:
            raise MyCommandProviderException()
            return CommandType.SHOW_COVER, {}

        application.process_command(command_provider=dummy)

        self.assertEqual(type(user_interface.exception), MyCommandProviderException)
