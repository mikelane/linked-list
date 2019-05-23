import logging

import pytest
from pytest_lambda import lambda_fixture, static_fixture

from linked_list import BasicLinearLinkedList

logger = logging.getLogger(__name__)

nodes = lambda_fixture(lambda single_link_node_factory: single_link_node_factory.create_batch(size=10))

empty_list = lambda_fixture(lambda: BasicLinearLinkedList())

items_to_add = static_fixture([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)])


@pytest.fixture
def list_with_nodes(nodes):
    for current, next_node in zip(nodes, nodes[1:]):
        current.next = next_node

    linear_linked_list = BasicLinearLinkedList()
    linear_linked_list.head = nodes[0]
    linear_linked_list.length = 10

    return linear_linked_list


class TestBasicLinearLinkedList:
    class ContextValidKey:
        @pytest.mark.parametrize(argnames=('key', 'value'), argvalues=[(1, 2), ('a', 'b')])
        class DescribePrependSingleItem:
            def it_prepend_to_empty_list(self, key, value, empty_list):
                assert len(empty_list) == 0
                assert empty_list.head is None

                empty_list.prepend(key, value)
                assert len(empty_list) == 1
                assert empty_list.head.key == key
                assert empty_list.head.value == value

            def it_prepend_to_list_with_existing_nodes(self, key, value, list_with_nodes):
                assert len(list_with_nodes) == 10
                assert list_with_nodes.head is not None

                list_with_nodes.prepend(key, value)
                assert len(list_with_nodes) == 11
                assert list_with_nodes.head.key == key
                assert list_with_nodes.head.value == value

        class DescribePrependMultipleItems:
            class ContextValidInputs:
                def it_adds_a_list_of_key_value_pairs(self, items_to_add, empty_list):
                    assert len(empty_list) == 0
                    assert empty_list.head is None

                    empty_list.add_all(items_to_add)
                    assert len(empty_list) == len(items_to_add)
                    assert empty_list.head.key == items_to_add[0][0]

                def it_constructs_list_when_passed_key_value_pairs(self, items_to_add):
                    the_list = BasicLinearLinkedList(items_to_add)
                    assert len(the_list) == len(items_to_add)
                    assert the_list.head.key == items_to_add[0][0]

            class ContextInvalidInputs:
                def it_will_raise_typeerror_if_items_is_not_iterable(self):
                    with pytest.raises(TypeError):
                        BasicLinearLinkedList(1)

                def it_will_raise_typeerror_if_items_are_not_key_value_pairs(self):
                    with pytest.raises(TypeError):
                        BasicLinearLinkedList([1])

    class ContextInvalidKey:
        def test_prepend(self, empty_list):
            assert len(empty_list) == 0
            assert empty_list.head is None

            with pytest.raises(TypeError):
                empty_list.prepend(['lists are not hashable'], 'this should cause a TypeError')
