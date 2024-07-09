# from inspect import signature
from random import randint

from faker import Faker


def rand_ratio():
    return randint(650, 750), randint(650, 750)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def make_book():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=250),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/books' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_book())