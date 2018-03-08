from abc import ABCMeta, abstractmethod
from typing import Optional

from brochure.values.basics import Basics
from brochure.values.section import Section


class BrochureUserInterface(metaclass=ABCMeta):

    @abstractmethod
    def show_unknown_command(self, basics: Basics) -> None:
        pass  # pragma: no cover

    @abstractmethod
    def show_cover(self, cover_section: Section, basics: Basics) -> None:
        pass  # pragma: no cover

    @abstractmethod
    def show_section(self, section: Section, basics: Basics) -> None:
        pass  # pragma: no cover

    @abstractmethod
    def show_unexpected_exception(self, exception: Exception, basics: Optional[Basics]) -> None:
        pass  # pragma: no cover
