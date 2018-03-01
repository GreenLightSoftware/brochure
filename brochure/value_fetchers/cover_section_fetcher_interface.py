from typing import Callable, Type

from brochure.values.section import Section

CoverSectionFetcherInterface = Type[Callable[[], Section]]
