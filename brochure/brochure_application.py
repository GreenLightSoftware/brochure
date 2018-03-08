from collections import defaultdict
from functools import partial
from typing import Optional

from brochure.brochure_user_interface import BrochureUserInterface
from brochure.commands.command_provider_interface import CommandProviderInterface
from brochure.commands.command_types import CommandType
from brochure.value_fetchers.basics_fetcher import BasicsFetcher
from brochure.value_fetchers.contact_method_fetcher_interface import ContactMethodFetcherInterface
from brochure.value_fetchers.section_repository_interface import SectionRepositoryInterface
from brochure.value_fetchers.enterprise_fetcher_interface import EnterpriseFetcherInterface


class BrochureApplication(object):
    def __init__(self,
                 contact_method_fetcher: ContactMethodFetcherInterface,
                 section_repository: SectionRepositoryInterface,
                 enterprise_fetcher: EnterpriseFetcherInterface) -> None:
        super().__init__()
        self._enterprise_fetcher = enterprise_fetcher
        self._section_repository = section_repository
        self._contact_method_fetcher = contact_method_fetcher
        self._user_interface = None
        self._basics_fetcher = BasicsFetcher(contact_methods_fetcher=self._contact_method_fetcher,
                                             enterprise_fetcher=self._enterprise_fetcher)

        self._command_map = defaultdict(lambda: self.show_unknown)
        self._command_map[CommandType.UNKNOWN] = self.show_unknown
        self._command_map[CommandType.SHOW_COVER] = self.show_cover
        self._command_map[CommandType.SHOW_SECTION] = self.show_section

    def process_command(self, command_provider: CommandProviderInterface):
        # noinspection PyBroadException
        try:
            command_type, command_parameters = command_provider()
            unbound_command_callable = self._command_map[command_type]
            command_callable = partial(unbound_command_callable, **command_parameters)

            command_callable()
        except Exception as e:
            self.show_exception(e)

        self._user_interface = None

    def register_user_interface(self, user_interface: Optional[BrochureUserInterface]):
        self._user_interface = user_interface

    def show_cover(self):
        basics = self._basics_fetcher()
        cover_section = self._section_repository.fetch_cover_section()
        self._user_interface.show_cover(cover_section=cover_section, basics=basics)

    def show_section(self, identifier: int):
        basics = self._basics_fetcher()
        section = self._section_repository.fetch_section(identifier=identifier)
        self._user_interface.show_section(section=section, basics=basics)

    def show_unknown(self):
        basics = self._basics_fetcher()
        self._user_interface.show_unknown_command(basics=basics)

    def show_exception(self, e):
        basics = None
        # noinspection PyBroadException
        try:
            basics = self._basics_fetcher()
        except Exception:
            pass

        self._user_interface.show_unexpected_exception(exception=e, basics=basics)
