from django.contrib import admin

from . models import Item,OrderItem,Order,Payment,Coupon,Refund,Address

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','ordered','being_delivered','received','refund_requested','refund_requested','billing_address','shipping_address','payment','coupon']
    list_display_links = ['billing_address','shipping_address','payment','coupon']
    list_filter = ['ordered','being_delivered','received','refund_requested','refund_requested']
    search_fields = ['user__username','ref_code']

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'appartment_address',
        'country',
        'zip',
        'address_type',
        'default',
    ]
    list_filter = ['default','address_type','country']
    search_fields = ['user','street_address','appartment_address','zip']


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Address, AddressAdmin)
admin.site.register(Refund)
