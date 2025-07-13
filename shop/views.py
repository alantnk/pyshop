from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from cart.forms import CartAddProductForm
from shop.models import Category, Product
from shop.recommender import Recommender


class ProductListView(TemplateView):
    template_name = 'shop/product/list.html'

    def get_context_data(self, **kwargs):
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        category_slug = kwargs.get('category_slug')
        if category_slug:
            lang = self.request.LANGUAGE_CODE
            category = get_object_or_404(
                Category,
                translations__language_code=lang,
                translations__slug=category_slug
            )
            products = products.filter(category=category)
        kwargs.update({
            'category': category,
            'categories': categories,
            'products': products
        })

        return kwargs


class ProductDetailView(TemplateView):
    template_name = 'shop/product/detail.html'

    def get_context_data(self, **kwargs):
        id = kwargs.get('id')
        slug = kwargs.get('slug')
        lang = self.request.LANGUAGE_CODE
        product = get_object_or_404(
            Product,
            id=id,
            translations__language_code=lang,
            translations__slug=slug, available=True
        )
        cart_product_form = CartAddProductForm()
        r = Recommender()
        recommended_products = r.suggest_products_for([product], 4)
        kwargs.update({
            'product': product,
            'cart_product_form': cart_product_form,
            'recommended_products': recommended_products
        })

        return kwargs
