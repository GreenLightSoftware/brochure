from brochure.value_fetchers.section_repository_interface import SectionRepositoryInterface
from brochure.values.section import Section


class ReferenceSectionRepository(SectionRepositoryInterface):

    def __init__(self) -> None:
        super().__init__()
        self._sections = {}
        self._cover_section_identifier = None
        self._identifier = 1

    def create_cover_section(self, title: str, body: str) -> int:
        identifier = self._identifier
        self._cover_section_identifier = identifier
        self._sections[identifier] = {"title": title, "body": body, "parent_section_identifier": None}
        self._identifier += 1

        return identifier

    def create_section(self, title: str, body: str, parent_section_identifier: int) -> int:
        identifier = self._identifier
        self._sections[identifier] = {"title": title, "body": body, "parent_section_identifier": parent_section_identifier}
        self._identifier += 1

        return identifier

    def fetch_cover_section(self) -> Section:
        cover_section_identifier = self._cover_section_identifier
        cover_section_fields = self._sections[cover_section_identifier]

        return Section(identifier=cover_section_identifier, **cover_section_fields)

    def fetch_section(self, identifier: int) -> Section:
        section_fields = self._sections[identifier]

        return Section(identifier=identifier, **section_fields)
