from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books.index"),
    path('simple/query', views.simple_query, name="books.simple_query"),
    path('complex/query', views.complex_query, name="books.complex_query"),
    path('lab8/task1', views.lab8_task1, name="books.lab8.task1"),
    path('lab8/task2', views.lab8_task2, name="books.lab8.task2"),
    path('lab8/task3', views.lab8_task3, name="books.lab8.task3"),
    path('lab8/task4', views.lab8_task4, name="books.lab8.task4"),
    path('lab8/task5', views.lab8_task5, name="books.lab8.task5"),
    path('lab8/task7', views.lab8_task7, name="books.lab8.task7"),
    path('lab9/task1', views.lab9_task1, name="books.lab9.task1"),
    path('lab9/task2', views.lab9_task2, name="books.lab9.task2"),
    path('lab9/task3', views.lab9_task3, name="books.lab9.task3"),
    path('lab9/task4', views.lab9_task4, name="books.lab9.task4"),
    path('lab9/task5', views.lab9_task5, name="books.lab9.task5"),
    path('lab9/task6', views.lab9_task6, name="books.lab9.task6"),
    # Lab 10 Part 1 CRUD
    path('lab9_part1/listbooks', views.lab9_part1_listbooks, name="books.lab9_part1.listbooks"),
    path('lab9_part1/addbook', views.lab9_part1_addbook, name="books.lab9_part1.addbook"),
    path('lab9_part1/editbook/<int:book_id>', views.lab9_part1_editbook, name="books.lab9_part1.editbook"),
    path('lab9_part1/deletebook/<int:book_id>', views.lab9_part1_deletebook, name="books.lab9_part1.deletebook"),
    # Lab 10 Part 2 CRUD with Django forms
    path('lab9_part2/listbooks', views.lab9_part2_listbooks, name="books.lab9_part2.listbooks"),
    path('lab9_part2/addbook', views.lab9_part2_addbook, name="books.lab9_part2.addbook"),
    path('lab9_part2/editbook/<int:book_id>', views.lab9_part2_editbook, name="books.lab9_part2.editbook"),
    path('lab9_part2/deletebook/<int:book_id>', views.lab9_part2_deletebook, name="books.lab9_part2.deletebook"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links', views.html5_links, name="books.html5.links"),
    path('html5/text/formatting', views.html5_text_formatting, name="books.html5.text.formatting"),
    path('html5/listing', views.html5_listing, name="books.html5.listing"),
    path('html5/tables', views.html5_tables, name="books.html5.tables"),
    path('search', views.search_books, name="books.search"),
]
