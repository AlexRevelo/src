from django.shortcuts import render


def about(request):
	return render(request, "about.html", {})

def book_delete(request, pk, template_name='newsletter/server_confirm_delete.html'):
    book= get_object_or_404(Book, pk=pk)    
    if request.method=='POST':
        book.delete()
        return redirect('books_fbv:book_list')
    return render(request, template_name, {'object':book})
