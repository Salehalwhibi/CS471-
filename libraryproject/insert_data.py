from apps.bookmodule.models import Book

# Insert the books data
book1 = Book(title='Continuous Delivery', author='J.Humble and D. Farley', price=120.00, edition=3)
book1.save()

book2 = Book(title='Reversing: Secrets of Reverse Engineering', author='E. Eilam', price=97.00, edition=2)
book2.save()

book3 = Book(title='The Hundred-Page Machine Learning Book', author='Andriy Burkov', price=100.00, edition=4)
book3.save()

# Verify the data
books = Book.objects.all()
for book in books:
    print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Price: {book.price}, Edition: {book.edition}")
