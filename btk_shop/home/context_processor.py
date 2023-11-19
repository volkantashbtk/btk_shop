from home.models import Setting
from product.models import Category

def category(request):
    return {'category': Category.objects.all()}

def setting(request):
    return {'setting': Setting.objects.all()}

# context_processor ile tüm sayfalarda ortak kontext tanımları yapılıyor.
# sonra projenin setting.py içinde options içinde tanıtmak gerekiyor.