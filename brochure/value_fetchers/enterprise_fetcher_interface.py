from typing import Callable, Type

from brochure.values.enterprise import Enterprise

EnterpriseFetcherInterface = Type[Callable[[], Enterprise]]
