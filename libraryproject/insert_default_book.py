import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libraryproject.settings')
django.setup()
from apps.bookmodule.models import Book

if not Book.objects.exists():
    Book.objects.create(
        title='Test Book',
        author='Test Author',
        price=10.0,
        edition=1,
        quantity=5
    )
    print('Default book created.')
else:
    print('Books already exist.')