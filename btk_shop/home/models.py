from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import TextInput, Textarea, ModelForm

# Create your models here.
class Setting(models.Model):
    STATUS = (('True', 'Evet'), ('False', 'Hayır'),)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    adress = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=50)
    smtpemail = models.CharField(blank=True, max_length=50)
    smtppassword = models.CharField(blank=True, max_length=50)
    smtpport = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    aboutus = RichTextUploadingField()
    contact = RichTextUploadingField()
    references = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    
    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True, max_length=255)
    status = models.CharField(blank=True, max_length=10, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
# class ContactForm(ModelForm):
#     class Meta:
#         model = ContactFormMessage
#         fields = ['name', 'email', 'subject', 'message']
#         widgets = {
#             'name'    : TextInput(attrs={'class': 'input', 'placeholde': 'Name & Surname'}),
#             'subject' : TextInput(attrs={'class': 'input', 'placeholde': 'Subject'}),
#             'email'   : TextInput(attrs={'class': 'input', 'placeholde': 'Email Address'}),
#             'message' : Textarea(attrs={'class': 'input', 'placeholde': 'Your Message', 'row':'5'}),
#         }

class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(
                attrs={
                    'type'          : "text",
                    'class'         : "form-control", 
                    'id'            : "name", 
                    'placeholder'   : "Your Name", 
                    'required'      : "required",
                    'data-validation-required-message' : "Please enter your name"
                    }),
            'email': TextInput(
                attrs={
                    'type'          : 'email',
                    'class'         : "form-control",
                    'id'            : "email",
                    'placeholder'   : "Your Email",
                    'required'      : "required",
                    'data-validation-required-message': "Please enter your email"
                    }),
            'subject': TextInput(
                attrs={
                    'type'          : "text", 
                    'class'         : "form-control", 
                    'id'            : "subject", 
                    'placeholder'   : "Subject",                       
                    'required'      : "required", 
                    'data-validation-required-message': "Please enter a subject"}),
            'message': Textarea(
                attrs={
                    'class'         : "form-control", 
                    'rows'          : "6", 
                    'id'            : "message", 
                    'placeholder'   : "Message",
                    'required'      : "required",
                    'data-validation-required-message': "Please enter your message"}),
        }
