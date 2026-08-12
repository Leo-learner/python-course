from contacts_oop import ContactBook, ContactNotFound
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
    with pytest.raises(ContactNotFound):
        book.find("李四")

def test_two_book_are_independent():
    book = ContactBook()
    book.add("王五", "150")
    book2 = ContactBook()
    book2.add("小明", "160")
    with pytest.raises(ContactNotFound):
        book.find("小明")
    assert book.find("王五") == "150"
    with pytest.raises(ContactNotFound):
        book2.find("王五")
    assert book2.find("小明") == "160"

def test_add_duplicate_overwrites():
    book = ContactBook()
    book.add("张三", "138")
    book.add("张三", "139")
    assert book.find("张三") == "139"
    assert len(book.show_all()) == 1

def test_show_all_returns_a_copy():
    book = ContactBook()
    book.add("张三", "138")
    data = book.show_all()
    data.clear()
    assert book.find("张三") == "138"

def test_delete_not_exists():
    book = ContactBook()
    with pytest.raises(ContactNotFound):
        book.delete("张三")

def test_check():
    book = ContactBook()
    book.add("张三", "139")
    assert book.check("张三")
    assert not book.check("李四")