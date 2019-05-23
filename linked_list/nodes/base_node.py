import functools
from collections.abc import Hashable


@functools.total_ordering
class Node:
    def __init__(self, key, value):
        if not isinstance(key, Hashable):
            raise TypeError('Keys must be hashable!')
        self.key = key
        self.value = value

    def __str__(self):
        return f'[key: {self.key!s}, value: {self.value!s}]'

    def __repr__(self):
        return f'Node(key={self.key}, value={self.value})'

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

    def __hash__(self):
        return hash(self.key)
