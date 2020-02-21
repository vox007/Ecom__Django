from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . views import(
    ItemDetailView,
    CheckoutView,
    HomeView,
    add_to_cart,
    remove_from_cart,
    OrderSummaryView,
    remove_cart,
    PaymentView,
    AddCouponView,
    RequestRefund,

)

app_name = 'core'
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('checkout/',CheckoutView.as_view(),name='checkout'),
    path('product/<slug>/',ItemDetailView.as_view(),name='product'),
    path('add-to-cart/<slug>/',add_to_cart,name='add-to-cart'),
    path('add-coupon/',AddCouponView.as_view(),name='add-coupon'),
    path('remove-from-cart/<slug>/',remove_from_cart,name='remove-from-cart'),
    path('order-summary/',OrderSummaryView.as_view(),name='order-summary'),
    path('remove-cart/<slug>/',remove_cart,name='remove-cart'),
    path('payment/<payment_option>/',PaymentView.as_view(),name='payment'),
    path('request-refund',RequestRefund.as_view(),name="request-refund")



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
