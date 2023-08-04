import datetime
from .Customer import Customer

def start():
    
    print("hello world")
    steve = Customer(
        first_name = "Steve",
        last_name = "Lorello",
        email="foo@bar.com",
        join_date = datetime.date.today(),
        age=34,
        bio="Senior Field Engineer at Redis"
    )
    print(steve.pk)
    print('goodbye world')