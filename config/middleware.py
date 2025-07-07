import threading

TENANT_DB = threading.local()

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant_db = request.headers.get('X-TENANT')
        if tenant_db:
            TENANT_DB.name = tenant_db
        else:
            TENANT_DB.name = None
        return self.get_response(request)

def get_current_tenant_db():
    return getattr(TENANT_DB, 'name', None)
