n = int(input())
books = dict()

for _ in range(n):
    book = input()
    if book not in books.keys():
        books[book] =1
    else:
        books[book]+=1

books_list = list(books.items())
books_list = sorted(books_list, key=lambda x :(-x[1],x[0]))     

print(books_list[0][0])