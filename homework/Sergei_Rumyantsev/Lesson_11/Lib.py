class Book:
    page_material = "Бумага"
    has_text = True
    

    def __init__(self, book_name, author, num_pages, isbn, is_reserved=False):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.is_reserved = is_reserved


    def display_info(self):
        info = (
            f"Название: {self.book_name}, "
            f"Автор: {self.author}, "
            f"страниц: {self.num_pages}, "
            f"материал: {self.page_material}"
        )
        if self.is_reserved:
            print(f"{info}, зарезервирована")
        else:
            print(info)


book1 = Book(book_name="Мастер и Маргарита", author="Михаил Булгаков", num_pages=480, isbn="978-5-17-104936-0")
book2 = Book(book_name="Идиот", author="Фёдор Достоевский", num_pages=640, isbn="978-5-389-10870-1")
book3 = Book(book_name="1984", author="Джордж Оруэлл", num_pages=320, isbn="978-5-17-087090-1", is_reserved = True)
book4 = Book(book_name="Гарри Поттер и философский камень", author="Джоан Роулинг", num_pages=399, isbn="978-5-389-13008-5")
book5 = Book(book_name="Убить пересмешника", author="Харпер Ли", num_pages=352, isbn="978-5-17-098522-3")


book1.display_info()
book2.display_info()
book3.display_info()
book4.display_info()
book5.display_info()

class Textbook(Book):
    is_task_available = True


    def __init__(self, book_name, author, num_pages, subject, class_number, is_reserved=False):
        super().__init__(book_name, author, num_pages, None, is_reserved)
        self.subject = subject
        self.class_number = class_number


    def display_info(self):
        info = (
            f"Название: {self.book_name}, "
            f"Автор: {self.author}, "
            f"страниц: {self.num_pages}, "
            f"предмет: {self.subject}, "
            f"класс: {self.class_number}"
        )
        if self.is_reserved:
            print(f"{info}, зарезервирована")
        else:
            print(info)

   
textbook_alg = Textbook(book_name = 'Алгебра', author = 'Иванов', num_pages = '200', subject = 'Математика', class_number = '9', is_reserved = True)
textbook_forlang = Textbook(book_name = 'Английский для начинающих', author = 'Сидоров', num_pages = '157', subject = 'Английский Язык', class_number = '2', is_reserved = False)
textbook_physics = Textbook(book_name = 'Учебник по физике', author = 'Карапетян', num_pages = '366', subject = 'Физика', class_number = '7', is_reserved = False)
textbook_cs = Textbook(book_name = 'Computer Science for beginners', author = 'Evans', num_pages = '266', subject = 'Информатика', class_number = '9', is_reserved = False)
textbook_hystory = Textbook(book_name = 'История России', author = 'Соколов', num_pages = '455', subject = 'Математика', class_number = '8', is_reserved = False)

textbook_alg.display_info()
textbook_forlang.display_info()
textbook_physics.display_info()
textbook_cs.display_info()
textbook_hystory.display_info()
