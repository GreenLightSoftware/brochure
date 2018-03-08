from typing import Tuple, Iterable, Dict
from unittest import TestCase

from brochure.brochure_application import BrochureApplication
from brochure.values.contact_method import ContactMethod
from brochure.values.enterprise import Enterprise
from brochure_reference_implementations.reference_contact_method_fetcher import ReferenceContactMethodFetcher
from brochure_reference_implementations.reference_enterprise_fetcher import ReferenceEnterpriseFetcher
from brochure_reference_implementations.reference_section_repository import ReferenceSectionRepository
from brochure_reference_implementations.reference_user_interface import ReferenceUserInterface


class BrochureApplicationTestCase(TestCase):
    @staticmethod
    def get_subject(expected_enterprise: Enterprise,
                    expected_contact_method: ContactMethod,
                    expected_cover_section_title: str,
                    expected_cover_section_body: str,
                    expected_sections: Iterable[Dict]) -> Tuple[BrochureApplication, ReferenceUserInterface]:
        section_repository = ReferenceSectionRepository()
        cover_section_identifier = section_repository.create_cover_section(title=expected_cover_section_title,
                                                                           body=expected_cover_section_body)
        [section_repository.create_section(parent_section_identifier=cover_section_identifier,
                                           **expected_section)for expected_section in expected_sections]
        contact_method_fetcher = ReferenceContactMethodFetcher(**expected_contact_method._asdict())
        enterprise_fetcher = ReferenceEnterpriseFetcher(**expected_enterprise._asdict())
        user_interface = ReferenceUserInterface()
        application = BrochureApplication(contact_method_fetcher=contact_method_fetcher,
                                          section_repository=section_repository,
                                          enterprise_fetcher=enterprise_fetcher)
        application.register_user_interface(user_interface=user_interface)

        return application, user_interface
