from rest_framework import generics
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import vendorSerializer, purchaseOrderSerializer, HistoricalPerformanceSerializer


class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = vendorSerializer
    lookup_field = 'pk'


class HistoricalPerformanceView(generics.ListAPIView):
    serializer_class = HistoricalPerformanceSerializer

    def get_queryset(self):
        vendor_id = self.kwargs['pk']
        return HistoricalPerformance.objects.filter(vendor_id=vendor_id)


class vendorListCreate(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = vendorSerializer

    def perform_create(self, serializer):
        serializer.save()


class vendorDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = vendorSerializer


class purchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = purchaseOrderSerializer

    def get_queryset(self):
        vendor_id = self.request.query_params.get('vendor_id')
        if vendor_id:
            return PurchaseOrder.objects.filter(vendor=vendor_id)
        return PurchaseOrder.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class vendorListView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = vendorSerializer


class purchaseOrderDetailView(generics.RetrieveAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = purchaseOrderSerializer


class purchaseOrderUpdateView(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = purchaseOrderSerializer


class purchaseOrderDeleteView(generics.DestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = purchaseOrderSerializer
