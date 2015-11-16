from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, SignUpForm
from .models import SignUp
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from newsletter.models import SignUp
# Create your views here.
def home(request):
	title = 'Contactenos'
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		#form.save()
		#print request.POST['email'] #not recommended
		instance = form.save(commit=False)

		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		# if not instance.full_name:
		# 	instance.full_name = "Justin"
		instance.save()
		context = {
			"title": "Gracias"
		}

	if request.user.is_authenticated() and request.user.is_staff:
		#print(SignUp.objects.all())
		# i = 1
		# for instance in SignUp.objects.all():
		# 	print(i)
		# 	print(instance.full_name)
		# 	i += 1

		queryset = SignUp.objects.all().order_by('-timestamp') #.filter(full_name__iexact="Justin")
		#print(SignUp.objects.all().order_by('-timestamp').filter(full_name__iexact="Justin").count())
		context = {
			"queryset": queryset
		}

	return render(request, "home.html", context)



def contact(request):
	title = 'Contactenos'

	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
		# 	#print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("Mensaje")
		form_full_name = form.cleaned_data.get("Nombre")
		# print email, message, full_name
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'youotheremail@email.com']
		contact_message = "%s: %s via %s"%( 
				form_full_name, 
				form_message, 
				form_email)
		some_html_message = """
		<h1>hello</h1>
		"""
		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				html_message=some_html_message,
				fail_silently=True)

	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,
	}
	return render(request, "forms.html", context)

def book_delete(request, pk, template_name='newsletter/server_confirm_delete.html'):
    book= get_object_or_404(SignUp, pk=pk)    
    if request.method=='POST':
        book.delete()
        return redirect('home')
    return render(request, template_name, {'object':book})













