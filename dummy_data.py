import os,django

import random
from django.conf import settings

from library.models import Book,Author,Review
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

def create_books(n):
    fake = Faker()
    for x in range(n):
        Book.objects.create(
            title=fake.sentence(),
            author=Author.objects.all().order_by('?')[0],
            publication_date = fake.date_time_between(start_date='-1y', end_date='now'),
            price=random.randint(1010,2600)
        )



def create_Author(n):
    fake=Faker()
    for x in range(n):
        Author.objects.create(
            name=fake.name(),
            birth_date=fake.date_of_birth(),
            biography=fake.paragraph(),
    )


def create_Review(n):
    fake = Faker()
    for x in range(n):
        Review.objects.create(
            book=Book.objects.all().order_by('?')[0],
            reviewer_name=fake.name(),
            content=fake.paragraph(),
            rating=fake.random_int(min=0, max=5),
        )


create_books(5)