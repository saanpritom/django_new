import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project02.settings')

import django
django.setup()

import random
from testapp.models import AccessRecords, Topic, Webpage
from faker import Faker


fake = Faker()
topics_name = ['Media', 'Industry', 'Military', 'Space', 'Agriculture']

def populate_topic():
    new_data = Topic.objects.get_or_create(top_name=random.choice(topics_name))[0]
    print('New Topic Created')
    return new_data


def populate_rests(numbers):

    for entry in range(numbers):

        tcp_name = populate_topic()
        print('New Topic assigned as Foreign Key')

        webpg_name = fake.company()
        webpg_url = fake.url()
        webpg_date = fake.date()

        new_rest_data = Webpage.objects.get_or_create(topic=tcp_name, name=webpg_name, url=webpg_url)[0]
        print('New webpage data created')

        new_access_data = AccessRecords.objects.get_or_create(name=new_rest_data, date=webpg_date)[0]
        print('New access data created')


populate_rests(20)
print('Populated Tables')
