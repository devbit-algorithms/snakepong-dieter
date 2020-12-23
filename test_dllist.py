from dllist import DoubleLinkedList

def test_empty_list():
    list = DoubleLinkedList()
    assert list.isEmpty()

def test_add_element_to_front():
    list = DoubleLinkedList()
    list.addFront('First')
    assert not list.isEmpty()

def test_add_element_to_back():
    list = DoubleLinkedList()
    list.addFront('First')
    list.addBack('Second')
    assert list.front() == 'First'

def test_multiple_items_added():
    list = DoubleLinkedList()
    list.addFront('First').addBack('Last')
    assert list.front() == 'First'
    assert list.back() == 'Last'

def test_multiple_items_added_to_front():
    list = DoubleLinkedList()
    list.addFront('Last').addFront('First')
    assert list.front() == 'First'
    assert list.back() == 'Last'

def test_get_front_node():
    list = DoubleLinkedList()
    assert list.front() == None
    list.addFront("First")
    assert list.front() == "First"

def test_get_back_node():
    list = DoubleLinkedList()
    list.addFront("Second")
    assert list.back() == "Second"
    list.addFront("First")
    assert list.back() == "Second"

def test_remove_front():
    list = DoubleLinkedList()
    list.addFront('Last').addFront('First')
    assert list.removeFront() == "First"
    assert list.front() == "Last"
    assert list.removeFront() == "Last"
    assert list.isEmpty()

def test_remove_back():
    list = DoubleLinkedList()
    list.addFront('Last').addFront('First')
    assert list.removeBack() == "Last"
    assert list.front() == "First"
    assert list.back() == "First"
    assert list.removeBack() == "First"
    assert list.isEmpty()