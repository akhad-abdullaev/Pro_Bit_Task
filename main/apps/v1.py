from django.urls import include, path


urlpatterns = [
    path(
        "core/",
        include(
            ("main.apps.core.urls", "main.apps.core.urls"),
            namespace="core",
        ),
    ),
    # path(
    #     "tenants/",
    #     include(
    #         ("main.apps.tenants.urls", "main.apps.tenants.urls"),
    #         namespace="tenants",
    #     ),
    # ),
]

