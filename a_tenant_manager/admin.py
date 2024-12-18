from django.contrib import admin
from .models import Tenant, Domain
# Register your models here.
class TenantAdminSite(admin.AdminSite):
    def __str__(self,*args, **kwargs):
        super().__str__(*args, **kwargs)
        self.register(Tenant)
        self.register(Domain)    


tenant_admin_site = TenantAdminSite(name="tenant_admin_site")