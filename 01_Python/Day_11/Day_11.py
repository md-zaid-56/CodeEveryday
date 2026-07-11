
print("===== enumerate() =====")
books = [
    "Python",
    "C++",
    "Machine Learning",
    "SQL"
]
for index, book in enumerate(books, start=1):
    print(f"Book {index} : {book}")

print("\n===== any() =====")
available = [False, False, True, False]
if any(available):
    print("At least one book is available.")
else:
    print("No books are available.")

print("\n===== all() =====")
returned = [True, True, True, False]
if all(returned):
    print("All books have been returned.")
else:
    print("Some books are still pending.")