from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50,unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    avrage_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    

class PurchaseOrder(models.Model):
    STATUS_CHOISES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    po_number = models.CharField(max_length=255,unique=True)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20,choices=STATUS_CHOISES,default='pending')
    quality_rating = models.FloatField(null=True,blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"PurchaseOrder {self.po_number} - {self.vendor.name}"
    


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    quality_rating_avg = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])