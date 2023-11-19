from django.urls import path
from . import views
urlpatterns = [
    # ex: /polls/

    path("", views.index, name="index"),
    path("hakkimizda", views.hakkimizda, name="hakkimizda"),
    path("referanslar", views.hakkimizda, name="referanslar"),
    path("iletishim", views.iletishim, name="iletishim"),
    path("category/<int:id>/<slug:slug>", views.categoryProducts, name="categoryProducts"),
    path("product_detail/<int:id>/<slug:slug>", views.productDetail, name="productDetail"),

    # ex: /polls/5/
    # path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]