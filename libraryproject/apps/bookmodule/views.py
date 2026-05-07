from django.shortcuts import render
from django.db.models import Avg, Count, Max, Min, Q, Sum

from .models import Book, Publisher, Student

# Lab 10 Part 2 CRUD with Django forms
from .forms import BookForm
# Lab 10 Part 2 CRUD with Django forms
def lab9_part2_listbooks(request):
    books = Book.objects.all().order_by('id')
    return render(request, 'bookmodule/lab9_part2_listbooks.html', {'books': books})

def lab9_part2_addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books.lab9_part2.listbooks')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab9_part2_addbook.html', {'form': form})

def lab9_part2_editbook(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books.lab9_part2.listbooks')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab9_part2_editbook.html', {'form': form, 'book': book})

def lab9_part2_deletebook(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('books.lab9_part2.listbooks')
    return render(request, 'bookmodule/lab9_part2_deletebook.html', {'book': book})

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def html5_links(request):
    return render(request, 'bookmodule/html5_links.html')

def html5_text_formatting(request):
    return render(request, 'bookmodule/html5_text_formatting.html')

def html5_listing(request):
    return render(request, 'bookmodule/html5_listing.html')

def html5_tables(request):
    return render(request, 'bookmodule/html5_tables.html')

def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            if contained:
                newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    
    return render(request, 'bookmodule/searchForm.html')


def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False)\
        .filter(title__icontains='and')\
        .filter(edition__gte=2)\
        .exclude(price__lte=100)[:10]

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    return render(request, 'bookmodule/index.html')


def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8_task1.html', {'books': books})


def lab8_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/lab8_task2.html', {'books': books})


def lab8_task3(request):
    books = Book.objects.filter(
        Q(edition__lte=3) & (~Q(title__icontains='qu') | ~Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/lab8_task3.html', {'books': books})


def lab8_task4(request):
    books = Book.objects.order_by('title')
    return render(request, 'bookmodule/lab8_task4.html', {'books': books})


def lab8_task5(request):
    stats = Book.objects.aggregate(
        book_count=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price'),
    )
    return render(request, 'bookmodule/lab8_task5.html', {'stats': stats})


def lab8_task7(request):
    city_stats = Student.objects.values('address__city').annotate(
        student_count=Count('id')
    ).order_by('address__city')
    return render(request, 'bookmodule/lab8_task7.html', {'city_stats': city_stats})


def lab9_task1(request):
    books = list(Book.objects.all().order_by('title'))
    total_books = Book.objects.count()
    for book in books:
        book.availability_percentage = int((book.quantity / total_books) * 100) if total_books else 0
    return render(request, 'bookmodule/lab9_task1.html', {'books': books, 'total_books': total_books})


def lab9_task2(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('books__quantity')).order_by('name')
    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})


def lab9_task3(request):
    publishers = Publisher.objects.annotate(oldest_pubdate=Min('books__pubdate')).order_by('name')
    for publisher in publishers:
        if publisher.oldest_pubdate:
            publisher.oldest_books = publisher.books.filter(pubdate=publisher.oldest_pubdate).order_by('title')
        else:
            publisher.oldest_books = []
    return render(request, 'bookmodule/lab9_task3.html', {'publishers': publishers})


def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('books__price'),
        min_price=Min('books__price'),
        max_price=Max('books__price'),
    ).order_by('name')
    return render(request, 'bookmodule/lab9_task4.html', {'publishers': publishers})


def lab9_task5(request):
    publishers = Publisher.objects.annotate(
        high_rated_books=Count('books', filter=Q(books__rating__gte=4))
    ).order_by('name')
    return render(request, 'bookmodule/lab9_task5.html', {'publishers': publishers})


def lab9_task6(request):
    publishers = Book.objects.filter(
        price__gt=50,
        quantity__gte=1,
        quantity__lt=5,
        publisher__isnull=False,
    ).values('publisher__name').annotate(book_count=Count('id')).order_by('publisher__name')
    return render(request, 'bookmodule/lab9_task6.html', {'publishers': publishers})

# Lab 10 Part 1 CRUD views (بدون Django forms)
from django.shortcuts import get_object_or_404, redirect

def lab9_part1_listbooks(request):
    books = Book.objects.all().order_by('id')
    return render(request, 'bookmodule/lab9_part1_listbooks.html', {'books': books})

def lab9_part1_addbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')
        quantity = request.POST.get('quantity', 1)
        Book.objects.create(
            title=title,
            author=author,
            price=price or 0.0,
            edition=edition or 1,
            quantity=quantity or 1
        )
        return redirect('books.lab9_part1.listbooks')
    return render(request, 'bookmodule/lab9_part1_addbook.html')

def lab9_part1_editbook(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price') or 0.0
        book.edition = request.POST.get('edition') or 1
        book.quantity = request.POST.get('quantity') or 1
        book.save()
        return redirect('books.lab9_part1.listbooks')
    return render(request, 'bookmodule/lab9_part1_editbook.html', {'book': book})

def lab9_part1_deletebook(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('books.lab9_part1.listbooks')
    return render(request, 'bookmodule/lab9_part1_deletebook.html', {'book': book})
