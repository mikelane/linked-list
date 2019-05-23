import factory

from linked_list.nodes import Node, SingleLinkNode
from tests.util import register_factory


@register_factory
class NodeFactory(factory.Factory):
    class Meta:
        model = Node

    key = factory.Faker('random_int')
    value = factory.Faker('sentence')


@register_factory
class SingleLinkNodeFactory(factory.Factory):
    class Meta:
        model = SingleLinkNode

    key = factory.Faker('random_int')
    value = factory.Faker('sentence')
    next = None
