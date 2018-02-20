from collections import defaultdict
from functools import partial
from typing import Optional, Dict, Callable

from brochure.commands.command_provider_interface import CommandProviderInterface
from brochure.commands.command_types import CommandType
from brochure.brochure_user_interface import BrochureUserInterface
from brochure.value_fetchers.basics_fetcher import BasicsFetcher
from brochure.value_fetchers.contact_method_fetcher_interface import ContactMethodFetcherInterface
from brochure.value_fetchers.enterprise_fetcher_interface import EnterpriseFetcherInterface


class BrochureApplication(object):
    def __init__(self,
                 contact_method_fetcher: ContactMethodFetcherInterface,
                 enterprise_fetcher: EnterpriseFetcherInterface) -> None:
        super().__init__()
        self._enterprise_fetcher = enterprise_fetcher
        self._contact_method_fetcher = contact_method_fetcher
        self._user_interface = None
        self._basics_fetcher = BasicsFetcher(contact_methods_fetcher=self._contact_method_fetcher,
                                             enterprise_fetcher=self._enterprise_fetcher)

        self._command_map = defaultdict(lambda: self.show_unknown)
        self._command_map[CommandType.UNKNOWN] = self.show_unknown
        self._command_map[CommandType.SHOW_BASICS] = self.show_basics

    def process_command(self, command_provider: CommandProviderInterface):
        # noinspection PyBroadException
        try:
            command_type, command_parameters = command_provider()
            domain_command_callable = self._bind(command_type=command_type,
                                                 command_parameters=command_parameters)
            domain_command_callable()
        except Exception as e:
            self.show_exception(e)

        self._user_interface = None

    def register_user_interface(self, user_interface: Optional[BrochureUserInterface]):
        self._user_interface = user_interface

    def show_basics(self):
        basics = self._basics_fetcher()
        self._user_interface.show_basics(basics)

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

    def _bind(self, command_type: CommandType, command_parameters: Dict) -> Callable:
        domain_command_callable = self._command_map[command_type]

        return partial(domain_command_callable, **command_parameters)
