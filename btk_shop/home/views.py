from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

from home.models import ContactForm, ContactFormMessage, Setting
from product.models import Category, Product

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
