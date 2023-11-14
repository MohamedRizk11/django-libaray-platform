import os
import django
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
sys.path.append("D:\\libraryplatform\\src")
django.setup()
import random
from django.conf import settings
from faker import Faker
from library.models import Book, Author, Review



def create_books(n):
    fake = Faker()
    images=['1.jpg','2.jpg','3.jpg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.png']
    for _ in range(n):
        author = Author.objects.order_by('?').first()
        Book.objects.create(
            title=fake.sentence(),
            author=author,
            publication_date=fake.date_time_between(start_date='-1y', end_date='now'),
            price=random.randint(1010, 2600),
            logo=f"books/{images[random.randint(0,9)]}"
        )

def create_authors(n):
    fake = Faker()
    for _ in range(n):
        Author.objects.create(
            name=fake.name(),
            birth_date=fake.date_of_birth(),
            biography=fake.paragraph(),
        )

def create_reviews(n):
    fake = Faker()
    for _ in range(n):
        book = Book.objects.order_by('?').first()
        Review.objects.create(
            book=book,
            reviewer_name=fake.name(),
            content=fake.paragraph(),
            rating=fake.random_int(min=0, max=5),
        )

# Usage examples:
create_authors(150)
create_books(400)
create_reviews(500)
