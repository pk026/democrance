from django.urls import include, path
from rest_framework.routers import DefaultRouter

from insurance.views import CustomerViewSet, PolicyHistoryView, PolicyViewSet

router = DefaultRouter()
router.register(r"quote", PolicyViewSet)
router.register(r"policies", PolicyViewSet)


urlpatterns = [
    path("api/v1/create_customer/", CustomerViewSet.as_view(), name="customer-create"),
    path(
        "api/v1/policies/<int:policy_id>/history/",
        PolicyHistoryView.as_view(),
        name="policy_history",
    ),
    path("api/v1/", include(router.urls)),
]
