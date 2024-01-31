from django.contrib import admin
from .models import Product, Client, Order


# Register your models here.
@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(count=0)


@admin.action(description="Товар оплачен")
def is_paid(modeladmin, request, queryset):
    queryset.update(is_paid=True)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'count', 'price']
    ordering = ['title', '-count']
    list_filter = ['add_date', 'price']
    search_fields = ['title', 'description']
    search_help_text = 'Поиск продукции по наименованию'
    actions = [reset_quantity]
    readonly_fields = ['add_date']
    fieldsets = [
        (
            'Продукт',
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'описание товара',
                'fields': ['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'count'],
            },
        ),

    ]


class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone']
    ordering = ['id']
    search_fields = ['name', 'phone']
    search_help_text = 'Поиск клиента по имени или телефону'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'order_sum', 'is_paid']
    ordering = ['-id']
    list_filter = ['order_date', 'order_sum', 'is_paid']
    search_fields = ['order_date']
    search_help_text = 'Поиск заказа по дате'
    actions = [is_paid]
    readonly_fields = ['order_date']
    fieldsets = [
        (
            'Клиент',
            {
                'classes': ['wide'],
                'fields': ['client'],
            },
        ),
        (
            'Продукция',
            {
                'classes': ['collapse'],
                'description': 'Продукция',
                'fields': ['product'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['order_sum', 'is_paid', ],
            },
        ),

    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
