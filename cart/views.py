from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View, TemplateView

from coupons.forms import CouponApplyForm
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


class CartAddView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product_id = kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            cart.add(
                product=product,
                quantity=cd['quantity'],
                override_quantity=cd['override']
            )
        return redirect('cart:cart_detail')


class CartRemoveView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product_id = kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart:cart_detail')


class CartDetailView(TemplateView):
    template_name = 'cart/detail.html'

    def get_context_data(self, **kwargs):
        cart = Cart(self.request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(
                initial={'quantity': item['quantity'], 'override': True}
            )
        coupon_apply_form = CouponApplyForm()
        kwargs.update({'cart': cart, 'coupon_apply_form': coupon_apply_form})
        return kwargs
