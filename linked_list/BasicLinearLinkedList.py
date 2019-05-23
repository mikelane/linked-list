import logging
from typing import Any, Hashable, Optional, Sequence, Tuple

from linked_list.nodes import SingleLinkNode

logger = logging.getLogger(__name__)

KeyValuePair = Tuple[Hashable, Any]


class BasicLinearLinkedList:
    """The most basic linked list implementation. This should serve as a
    decent starting point for most other types of lists.
    """

    def __init__(self, items: Optional[Sequence[KeyValuePair]] = None):
        self.head: Optional[SingleLinkNode] = None
        self.length: int = 0
        if items:
            try:
                self.append_many(items)
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

    def prepend(self, key: Hashable, value: Any) -> None:
        temp = SingleLinkNode(key=key, value=value, next=self.head)
        self.head = temp
        self.length += 1

    def prepend_many(self, items: Sequence[KeyValuePair]) -> None:
        """Prepends all items from a sequence to the list. Note, this
        operation is equivalent to a stack push, so it will reverse the
        sequence.
        """
        iter(items)  # Validates that items is an iterable
        for key, value in items:
            self.prepend(key, value)

    def append(self, key: Hashable, value: Any) -> None:
        """Traverse the list, if required, and add a node at the end. This
        is an O(N) operation since this list lacks a tail pointer.
        """
        to_add = SingleLinkNode(key, value)

        if self.head is None:
            self.head = to_add
            self.length += 1
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = to_add
            self.length += 1

    def append_many(self, items: Sequence[KeyValuePair]):
        """Append many is O(N+M) where N is the length of the list and
        M is the length of the items to insert.
        """
        iter(items)  # Validates that items is an iterable
        (tail_key, tail_value), *items = items
        tail = SingleLinkNode(tail_key, tail_value)

        if self.head is None:
            self.head = tail
        else:
            self.head.next = tail
        self.length += 1

        for key, value in items:
            tail.next = SingleLinkNode(key, value)
            tail = tail.next
            self.length += 1
