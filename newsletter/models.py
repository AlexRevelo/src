from django.db import models


# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	mensaje = models.CharField(max_length=255, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	def __unicode__(self): #Python 3.3 is __str__
		return self.email

class Book(models.Model):
    name = models.CharField(max_length=200)
    fecha_in = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_out = models.DateTimeField(auto_now_add=True, auto_now=False)


    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books_fbv:book_edit', kwargs={'pk': self.pk})