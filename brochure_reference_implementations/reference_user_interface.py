from typing import Optional

from brochure.brochure_user_interface import BrochureUserInterface
from brochure.values.basics import Basics
from brochure.values.section import Section


class ReferenceUserInterface(BrochureUserInterface):

    def __init__(self) -> None:
        super().__init__()
        self.cover_section = None
        self.section = None
        self.basics = None
        self.unknown_basics = None
        self.exception = None
        self.exception_basics = None

    def show_unknown_command(self, basics: Basics) -> None:
        self.unknown_basics = basics

    def show_cover(self, basics: Basics, cover_section: Section) -> None:
        self.basics = basics
        self.cover_section = cover_section

    def show_section(self, section: Section, basics: Basics) -> None:
        self.section = section
        self.basics = basics

    def show_unexpected_exception(self, exception: Exception, basics: Optional[Basics]) -> None:
        self.exception = exception
        self.exception_basics = basics
