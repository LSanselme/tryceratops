from __future__ import annotations

from typing import TYPE_CHECKING, Set, Type

from .base import BaseFixer
from .exception_block import LoggerErrorFixer, RaiseWithoutCauseFixer, VerboseReraiseFixer

if TYPE_CHECKING:
    from tryceratops.filters import GlobalFilter

FIXER_CLASSES: Set[Type[BaseFixer]] = {
    RaiseWithoutCauseFixer,
    VerboseReraiseFixer,
    LoggerErrorFixer,
}


def get_fixers_chain(global_filter: GlobalFilter) -> Set[BaseFixer]:
    fixers = {
        fixercls() for fixercls in FIXER_CLASSES if global_filter.should_run_processor(fixercls)
    }
    return fixers
