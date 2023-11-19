from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from home.forms import SearchForm, LoginForm, SignUpForm

from home.models import Setting, ContactForm, ContactFormMessage, UserProfileForm, UserProfile
from product.models import Category, Images, Product, Comment

from order.models import ShopCart

# Create your views here.
def index(request):
    slider = Product.objects.all()
    urunler = Product.objects.all()[:8]
    context = {'slider': slider,
               'urunler': urunler,
               'page': 'home'}
    return render(request, 'index.html', context)
    # return HttpResponse("Merhaba")

def hakkimizda(request):
    return render(request, 'hakkimizda.html')

def referanslar(request):
    context = {'page': 'referanslar'}
    return render(request, 'referanslar.html', context)

def iletishim(request):
    if request.method == 'POST':
        form = ContactForm(request.Post)
        if form.is_valid():
            data = ContactFormMessage()
            data.name       = form.cleaned_data['name']
            data.email      = form.changed_data['email']
            data.subject    = form.changed_data['subject']
            data.message    = form.changed_data['message']
            data.ip         = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Mesajınız düzene iletildi.')
            return HttpResponseRedirect('/iletishim')
        else:
            messages.warning(request, 'Mesajınız düzene iletilemedi.')
            return HttpResponseRedirect('/iletishim')

    form = ContactForm
    context = {
                'form'      : form,
                'page'      : 'iletishim',
              }
    return render(request, 'iletisim.html', context)

def categoryProducts(request, id, slug):
    urunKategori = Category.objects.get(pk=id)
    urunler = list(Product.objects.filter(category_id=id))

    # #1 Kategorinin alt kategorisi var ise bunun ürünlerini de gösterebilmek için bu bölümü yazdık.
    node = Category.objects.get(pk=id)
    children = Category.objects.add_related_count(node.get_children(),
                                                  Product,
                                                  'category',
                                                  'product_counts')
    for dd in children:
        a = list(Product.objects.filter(category_id=dd.id))
        urunler.extend(a)
    # 1#
    context = {'page': 'Kategori',
               'urunKategori': urunKategori,
               'urunler': urunler}
    return render(request, 'kategori_urunler.html', context)

def productDetail(request, id, slug):
    urun = Product.objects.get(pk=id)
    images = Images.objects.filter(product = urun)
    # print(request.get_full_path())
    # print(request.get_host())
    # print(request.build_absolute_uri())
    comments = Comment.objects.filter(product_id=id)
    context = {'page': 'Urun',
               'urun': urun,
               'images': images,
               'comments': comments
    }
    return render(request, 'urun_detay.html', context)


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            products = Product.objects.filter(title__icontains=query)
            context = {'urunler': products,
                       'query': query}
            return render(request, 'product_search.html', context)
    return HttpResponseRedirect('/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    category = Category.objects.all()
    if request.method == 'POST':  # check post
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                request.session['cart_items'] = ShopCart.objects.filter(user_id=user.id).count()
                messages.success(request, "Başarılı şekilde oturum açtınız {}".format(user.username))
                return HttpResponseRedirect('/login')
            else:
                messages.warning(request, "Girilen Bilgiler Hatalı Tekrar Deneyiniz {}".format(username))
                return HttpResponseRedirect('/login')

    setting = Setting.objects.get(pk=1)

    form = LoginForm
    context = {'setting': setting,
               'form': form,
               'category': category}
    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() #completed sign up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Create data in profile table for user
            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="images/users/user.png"
            data.save()
            # sonradan eklenecek kısım
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/signup')


    form = SignUpForm()
    category = Category.objects.all()
    setting = Setting.objects.all()
    context = {'category': category,
               'form': form,
               'setting':setting
               }
    return render(request, 'signup_form.html', context)

def userProfile_view(request):
    category = Category.objects.all()
    if request.method == 'POST':  # check post
        form = UserProfileForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()  # create relation with model
            data.name = form.cleaned_data['name']  # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # save data to table
            messages.success(request, "Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/user_profile')

    setting = Setting.objects.get(pk=1)

    form = UserProfileForm
    context = {'setting': setting,
               'form': form,
               'category': category}
    return render(request, 'userprofile.html', context)