from typing import NamedTuple, Type


class NamedTupleFetcherProvider(object):
    def __init__(self, named_tuple_type: Type[NamedTuple]):
        super().__init__()
        self._named_tuple_type = named_tuple_type

    def __call__(self, *args, **kwargs):
        return lambda: self._named_tuple_type(**kwargs)
