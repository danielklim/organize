from .confirm import Confirm
from .copy import Copy
from .delete import Delete
from .echo import Echo
from .macos_tags import MacOSTags
from .move import Move
from .python import Python
from .rename import Rename
from .shell import Shell
from .trash import Trash

ALL = {
    Confirm.name: Confirm,
    Copy.name: Copy,
    Delete.name: Delete,
    Echo.name: Echo,
    MacOSTags.name: MacOSTags,
    Move.name: Move,
    Python.name: Python,
    Rename.name: Rename,
    Shell.name: Shell,
    Trash.name: Trash,
}
