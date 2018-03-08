from typing import NamedTuple, Optional


class Section(NamedTuple):
    identifier: int
    parent_section_identifier: Optional[int]
    title: str
    body: str
