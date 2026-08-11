from contacts_oop import ContactBook
import pytest

def test_add_then_find():
    book = ContactBook()
    book.add("张三", "138")
    assert book.find("张三") == "138"

def test_new_book_is_empty():
    book = ContactBook()
    assert book.show_all() == {}

def test_delete_then_not_find():
    book = ContactBook()
    book.add("李四", "140")
    book.delete("李四")
    with pytest.raises(KeyError):
        book.find("李四")

def test_two_book_are_independent():
    book = ContactBook()
    book.add("王五", "150")
    book2 = ContactBook()
    book2.add("小明", "160")
    with pytest.raises(KeyError):
        book.find("小明")
    assert book.find("王五") == "150"
    with pytest.raises(KeyError):
            book2.find("王五")
    assert book2.find("小明") == "160"