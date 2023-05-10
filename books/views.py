from django.shortcuts import render, redirect, get_object_or_404

from .models import Book

from .forms import BookForm


# Vista listar los objetos.
def list_books(request):

    try:

        books = Book.objects.all().order_by('-creation_date')

        context = {
            'books': books
        }

        return render(request, 'list_books.html', context)

    except Exception:

        return render(request, 'errors.html')

        


# Vista para crear registros en la base de datos a través del formulario.
def create_book(request):

    # Instancia de BookForm
    form = BookForm()

    if request.method == "POST":

        form = BookForm(request.POST)

        if form.is_valid():

            book = Book(
                title=form.cleaned_data['title'],
                isbn=form.cleaned_data['isbn'],
                creation_date=form.cleaned_data['creation_date'],
                pages=form.cleaned_data['pages'],
                editorial=form.cleaned_data['editorial']
            )
            book.save()

            return redirect('/list_books/')

        else:
            return redirect('/list_books/')

    context = {'form': form}
    
    return render(request, 'create_books.html', context)



def update_book(request, book_id):

    try:

        book = Book.objects.get(id=book_id)

        context = {
            "book": book
        }

        if request.method == 'POST':

            book.title = request.POST['title']
            book.isbn = int(request.POST['isbn'])
            book.creation_date = request.POST['creation_date']
            book.editorial = request.POST['editorial']

            book.save()

        return render(request, "update_books.html", context)
    
    except Exception:

        return render(request, 'errors.html')


def delete_book(request, book_id):

    # Obtener la instancia del objeto y eliminarla.

    try:

        book = Book.objects.get(id=book_id)

        if request.method == 'POST':
            
            # Elimino el objeto.
            book.delete()

            return redirect('/delete_ok/')
        
        context = {
            'book': book
        }

        return render(request, 'delete_book.html', context)
    
    except Exception:

        return render(request, 'errors.html')


def delete_ok(request):

    return render(request, 'delete_ok.html')


def retrieve_book(request, book_id):

    try:

        book = Book.objects.get(id=book_id)

        context = {
            'book': book
        }

        return render(request, 'retrieve_book.html', context)
    
    except Exception:

        return render(request, 'errors.html')