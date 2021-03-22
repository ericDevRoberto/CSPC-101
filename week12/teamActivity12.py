with open("books_and_chapters.txt") as books:

    largest_scripture = ""
    largest_book = ""
    largest_chapters = 0

    print("[Doctrine and Covenants, Official Declaration, Pearl of Great Price, New Testament, Old Testament]")

    name = input("Choise a scripture: ").lower()

    for book in books:

        book_split = book.split(":")

        book = book_split[0]
        chapter = int(book_split[1])
        scripture = book_split[2].strip()

        if chapter > largest_chapters and scripture.lower() == name:

            largest_scripture = scripture
            largest_book = book
            largest_chapters = chapter

    print(f"\nScripture: {largest_scripture}, Book: {largest_book}, Chapters: {largest_chapters}")
