from django.shortcuts import render
from django.views.generic import DetailView
from .models import Notebook, Smartphone, CPU, GPU, Category, LatestProducts

def test(request):
    return render(
        request,
        'base.html',
        context={}

    )
def test_view(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    products = LatestProducts.objects.get_products_for_main_page('notebook', 'smartphone', 'cpu', 'gpu')
    contex = {
        'categories': categories,
        'products': products
    }
    return render(request, 'base.html', contex)

class ProductDetailView(DetailView):

    CT_MODEL_MODEL_CLASS = {
        'notebook': Notebook,
        'smartphone': Smartphone,
        'cpu': CPU,
        'gpu': GPU
    }
    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product_default.html'
    slug_url_kwarg = 'slug'

class CategoryDetailView(DetailView):
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'

