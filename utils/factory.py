from faker import Faker
import random
import time
from models.user import User
from models.contact import Contact

fake = Faker()

def random_contact():
    return Contact(
        name=fake.name(),
        lastName=fake.last_name(),
        email=fake.email(),
        phone=fake.numerify("#" * random.randint(10, 15)),
        address=fake.address()[:50],
        description=fake.text(max_nb_chars=200),
    )

def random_user():
    username = f"qa_{int(time.time())}_{fake.email()}"
    password = fake.password(
        length=random.randint(8, 15),
        special_chars=False,
        digits=True,
        upper_case=True,
        lower_case=True,
    )+"$"
    return User(username=username, password=password)
