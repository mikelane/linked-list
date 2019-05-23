import logging
from typing import Any, Hashable, Iterable, Optional, Tuple, Sequence

from linked_list.nodes import SingleLinkNode

logger = logging.getLogger(__name__)


class BasicLinearLinkedList:
    def __init__(self, items: Optional[Sequence[Tuple[Hashable, Any]]] = None):
        self.head: Optional[SingleLinkNode] = None
        self.length: int = 0
        if items:
            try:
                self.add_all(items)
            except TypeError as e:
                logger.error(f'TypeError: {e}')
                raise TypeError(e)

    def __len__(self):
        return self.length

    def __str__(self):
        result = []
        current: Optional[SingleLinkNode] = self.head

        while current:
            result.append(str(current))
            current = current.next

        return ''.join(result)

    def __repr__(self):
        return f'<BasicLinearLinkedList@{id(self)}: length={len(self)}>'

    def prepend(self, key, value):
        temp = SingleLinkNode(key=key, value=value, next=self.head)
        self.head = temp
        self.length += 1

    def add_all(self, items: Sequence[Tuple[Hashable, Any]]) -> None:
        iter(items)  # Validates that items is iterable
        for key, value in reversed(items):
            self.prepend(key, value)
