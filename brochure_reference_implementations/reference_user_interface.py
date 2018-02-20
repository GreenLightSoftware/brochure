from typing import Optional

from brochure.brochure_user_interface import BrochureUserInterface
from brochure.values.basics import Basics


class ReferenceUserInterface(BrochureUserInterface):

    def __init__(self) -> None:
        super().__init__()
        self.basics = None
        self.unknown_basics = None
        self.exception = None
        self.exception_basics = None

    def show_unknown_command(self, basics: Basics) -> None:
        self.unknown_basics = basics

    def show_basics(self, basics: Basics) -> None:
        self.basics = basics

    def show_unexpected_exception(self, exception: Exception, basics: Optional[Basics]) -> None:
        self.exception = exception
        self.exception_basics = basics
