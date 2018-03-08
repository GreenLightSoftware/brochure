from abc import ABCMeta, abstractmethod

from brochure.values.section import Section


class SectionRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def create_cover_section(self,
                             title: str,
                             body: str) -> int:  # pragma: no cover
        pass

    @abstractmethod
    def create_section(self,
                       title: str,
                       body: str,
                       parent_section_identifier: int) -> int:  # pragma: no cover
        pass

    @abstractmethod
    def fetch_cover_section(self) -> Section:  # pragma: no cover
        pass

    @abstractmethod
    def fetch_section(self, identifier: int) -> Section:  # pragma: no cover
        pass
