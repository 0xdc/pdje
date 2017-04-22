from django.contrib import admin

from .models import *
# Register your models here.

class AliasInline(admin.TabularInline):
    model = Alias
    extra = 1
    verbose_name_plural = "Aliases"

class DkimInline(admin.StackedInline):
    model = DkimDomain
    extra = 0
    verbose_name_plural = "DKIM"
    verbose_name = "Selector"

class SenderCredentialInline(admin.StackedInline):
    model = SenderCredential
    extra = 0

class RecipientAdmin(admin.ModelAdmin):
    list_display = ["action", "address", "message"]

class DomainAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ["name", "aliases", "selectors"]
    inlines = [DkimInline, SenderCredentialInline, AliasInline]

admin.site.register(Domain, DomainAdmin)
admin.site.register(User)
admin.site.register(Recipient, RecipientAdmin)
