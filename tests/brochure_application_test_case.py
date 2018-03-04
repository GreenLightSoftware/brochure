from typing import Tuple
from unittest import TestCase

from brochure.brochure_application import BrochureApplication
from brochure.values.contact_method import ContactMethod
from brochure.values.enterprise import Enterprise
from brochure.values.section import Section
from brochure_reference_implementations.named_tuple_fetcher_provider import NamedTupleFetcherProvider
from brochure_reference_implementations.reference_contact_method_fetcher import ReferenceContactMethodFetcher
from brochure_reference_implementations.reference_enterprise_fetcher import ReferenceEnterpriseFetcher
from brochure_reference_implementations.reference_user_interface import ReferenceUserInterface

ReferenceCoverSectionFetcher = NamedTupleFetcherProvider(named_tuple_type=Section)


class BrochureApplicationTestCase(TestCase):
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
