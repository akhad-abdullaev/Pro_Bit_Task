from .middleware import get_current_tenant_db

class MultiTenantRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == "tenants":
            return get_current_tenant_db()
        return "default"

    def db_for_write(self, model, **hints):
        if model._meta.app_label == "tenants":
            return get_current_tenant_db()
        return "default"

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        tenant_db = get_current_tenant_db()
        if app_label == "tenants":
            return db == tenant_db
        return db == "default"
