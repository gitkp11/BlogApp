import os, django, random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "avsblog.settings")
django.setup()

from faker import Faker
from blog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


def create_post(N):
	fake = Faker()
	for x in range(4,N):
	    id = random.choice([1,2,3,4,5])
	    title = fake.name()
	    user = User.objects.create_user(    username    =   "test"+str(x),
	                                        email       =   "test"+str(x)+"@email.com",
	                                        password    =   "test"+str(x)+"password123"
	                                    )
	    Post.objects.create(    title   =   title+" Post!!!",
	                            author  =   User.objects.get(id=id),
	                            slug    =   "-".join(title.lower().split()),
	                            body    =   fake.text(),
	                            created =   timezone.now(),
	                            updated =   timezone.now(),
	                            status  =   'published',
	                        )

create_post(10)
print("DATA IS POPULATED SUCCESSFULLY.")
