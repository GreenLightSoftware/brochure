from typing import Callable, Tuple, Dict

from brochure.commands.command_types import CommandType

CommandProviderInterface = Callable[[], Tuple[CommandType, Dict]]
