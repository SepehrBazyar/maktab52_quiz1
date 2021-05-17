import dill
with open('books.dill', 'rb') as fl:
    books = dill.load(fl)

p1 = sorted(books, key = lambda x: x.ISBN)
p2 = sorted(books, key = lambda x: x.name)
p3 = sorted(books, key = lambda x: x.publish_date, reverse = True)

p4 = list(filter(books, lambda x: x.author == 'George Orwell'))
