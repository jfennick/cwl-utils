# NOTE: This dynamically typed stub was automatically generated by stubgen.

from os import PathLike
from typing import Any, Callable, Union

from ..cache import BaseCache as BaseCache
from ..controller import CacheController as CacheController

class FileCache(BaseCache):
    directory = ...  # type: Union[str, PathLike[str]]
    forever = ...  # type: bool
    filemode = ...  # type: str
    dirmode = ...  # type: str
    lock_class = ...  # type: Callable
    def __init__(self, directory: Union[str, PathLike[str]], forever=False, filemode=384, dirmode=448, use_dir_lock=None, lock_class=None) -> None: ...
    @staticmethod
    def encode(x): ...
    def get(self, key): ...
    def set(self, key, value): ...
    def delete(self, key): ...

def url_to_file_path(url, filecache): ...
