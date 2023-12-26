from django.urls import path
from .views import (
    VendorPerformanceView,
    HistoricalPerformanceView,
    purchaseOrderDeleteView,
    purchaseOrderDetailView,
    purchaseOrderListCreateView,
    purchaseOrderUpdateView,
    vendorDetailUpdateDeleteView,
    vendorListCreate,
)

urlpatterns = [
    path('api/vendors/', vendorListCreate.as_view(), name='vendor-create'),
    path('api/vendors/<int:pk>/', vendorDetailUpdateDeleteView.as_view(), name='vendor-detail-update-delete'),
    path('api/vendors/<int:pk>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
    path('api/vendors/<int:pk>/historical-performance/', HistoricalPerformanceView.as_view(), name='historical-performance'),
    path('api/purchase_orders/', purchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('api/purchase_orders/<int:pk>/', purchaseOrderDetailView.as_view(), name='purchase-order-detail'),
    path('api/purchase_orders/<int:pk>/update/', purchaseOrderUpdateView.as_view(), name='purchase-order-update'),
    path('api/purchase_orders/<int:pk>/delete/', purchaseOrderDeleteView.as_view(), name='purchase-order-delete'),
]
