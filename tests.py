import pytest
from main import BooksCollector


@pytest.fixture
def collector():   
    return BooksCollector()


class TestBooksCollector:
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2


    def test_add_new_book_more_than_40_characters(self, collector):
        name= 'a' * 41
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()


    @pytest.mark.parametrize('name', [ 'a', 'a' * 40 ]) 
    def test_add_new_book_valid_name_length(self, collector, name):
        collector.add_new_book(name)
        assert name in collector.get_books_genre()


    def test_set_book_genre_valid(self, collector):
        collector.add_new_book("Чернокнижник Гарри")
        collector.set_book_genre("Чернокнижник Гарри", "Фантастика")
        assert collector.get_book_genre("Чернокнижник Гарри") == "Фантастика"


    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book("Безыменный раб")
        collector.set_book_genre("Безыменный раб", "Роман")
        assert collector.get_book_genre("Безыменный раб") == ""


    def test_get_books_for_children(self, collector):
        collector.add_new_book("Гарри Поттер и философский камень")
        collector.set_book_genre("Гарри Поттер и философский камень", "Фантастика")
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")
        children_books = collector.get_books_for_children()
        assert "Гарри Поттер и философский камень" in children_books
        assert "Оно" not in children_books


    def test_add_book_in_favorites_no_duplicates(self, collector):
        collector.add_new_book("Система становление")
        collector.add_book_in_favorites("Система становление")
        collector.add_book_in_favorites("Система становление")
        favorites = collector.get_list_of_favorites_books()
        assert favorites.count("Система становление") == 1


    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Система становление")
        collector.add_book_in_favorites("Система становление")
        collector.delete_book_from_favorites("Система становление")
        favorites = collector.get_list_of_favorites_books()
        assert "Система становление" not in favorites


    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Гарри Поттер и философский камень")
        collector.set_book_genre("Гарри Поттер и философский камень", "Фантастика")
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")
        fantasy_books = collector.get_books_with_specific_genre("Фантастика")
        assert "Гарри Поттер и философский камень" in fantasy_books
        assert "Оно" not in fantasy_books