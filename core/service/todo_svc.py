from core.models import Todo, City, Person, Book, Video, Tutorial

def add_todo(new_task):
    todo = Todo(description=new_task)
    todo.save()
    return todo.to_dict_json()


def list_todos():
    todos = Todo.objects.all()
    b = Book.objects.select_related('author__hometown').get(id=1)
    p = b.author  # Doesn't hit the database.
    c = p.hometown  # Doesn't hit the database.
    livro_autor = b.author.hometown.name

    books_author = Book.objects.select_related('author__hometown').filter(author=1)
    autor_name = [{'autor': a.author.name, 'livro': a.name, 'cidade': a.author.hometown.name} for a in books_author]
    autor_cidade = Person.objects.select_related('hometown').get(id=1)
    cidade = autor_cidade.hometown.name


    # Without select_related()...
    d = Book.objects.get(id=1)  # Hits the database.
    e = d.author  # Hits the database.
    f = e.hometown

    # many to many
    # testea de melhor uso de orm do django

    tutorial = Tutorial.objects.prefetch_related('videos').get(id=4)
    video = [v.title for v in tutorial.videos.all()]

    return [todo.to_dict_json() for todo in todos]