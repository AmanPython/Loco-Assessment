from django.db import models
from transaction.base import BaseModel

# Create your models here.

class Transaction(BaseModel):
    transaction_id = models.IntegerField(null=False,blank=False)
    type = models.CharField(max_length=255, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.type} - {self.amount}"