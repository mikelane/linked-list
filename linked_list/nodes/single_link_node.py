from linked_list.nodes.base_node import Node


class SingleLinkNode(Node):
    def __init__(self, key, value, next=None):
        super().__init__(key=key, value=value)
        self.next = next

    def __str__(self):
        next_arrow = ' -> ' if self.next else ' -> X'
        return f'{super().__str__()}{next_arrow}'

    def __repr__(self):
        next_node = (
            f'<SingleLinkNode@{id(self.next)}: key={self.next.key}, ' f'value={self.next.value}>'
            if self.next
            else None
        )
        return f'SingleLinkNode(key={self.key}, value={self.value}) -> {next_node}'
