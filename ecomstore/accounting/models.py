from django.db import models
from ecomstore.catalog.models import RichTextField

# Create your models here.

class AllAccounts(models.Model):
    bank_name = models.CharField(max_length=40)
    account_number = models.CharField(max_length=20)
    account_type = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    url = models.CharField(max_length=30)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField()

    class Meta:
         db_table = "all_accounts"
         ordering = ['bank_name']

    def __str__(self):
        return self.account_number

    def __unicode__(self):
         return self.account_number

class BusinessEntity(models.Model):
    business_name = models.CharField(max_length=40)
    federal_tax_id = models.CharField(max_length=10)
    banking_source = models.CharField(max_length=20)
    bank_account_number = models.CharField(max_length=30)
    description = models.TextField()

    class Meta:
         db_table = "business_entity"
         ordering = ['business_name']


    def __str__(self):
        return self.business_name
    def __unicode__(self):
         return self.business_name

def get_business_entity():
    return BusinessEntity.objects.get(id=1)


FEDERAL_TAXES_941_944 = 1
FEDERAL_UNEMPL_940 = 2
NC_UNEMPL_TAX = 3
NC_INCOME_TAX = 4
PENALTY = 5
# set of possible order statuses
TAX_TYPE = ((FEDERAL_TAXES_941_944,'Federal Taxes 941/944'),
            (FEDERAL_UNEMPL_940,'Federal Unemployment Tax 940'),
            (NC_UNEMPL_TAX,'NC Unemployment Tax'),
            (NC_INCOME_TAX,'NC Income Tax'),
            (PENALTY,'Penalty'),)

Q1 = 1
Q2 = 2
Q3 = 3
Q4 = 4
TAX_PERIOD = ((Q1,'Q1'),
            (Q2,'Q2'),
            (Q3,'Q3'),
            (Q4,'Q4'),)

YEAR_2015 = 1
YEAR_2016 = 2
YEAR_2017 = 3
YEAR_2018 = 4
YEAR_2019 = 5
YEAR_2020 = 6
YEAR_2021 = 7
TAX_YEAR = ((YEAR_2015,'2015'),
            (YEAR_2016,'2016'),
            (YEAR_2017,'2017'),
            (YEAR_2018,'2018'),
            (YEAR_2019,'2019'),
            (YEAR_2020,'2020'),
            (YEAR_2021,'2021'),)



class TaxDue(models.Model):
    tax_type = models.IntegerField(choices=TAX_TYPE, default=FEDERAL_TAXES_941_944)
    tax_period = models.IntegerField(choices=TAX_PERIOD, default=Q1)
    tax_year = models.IntegerField(choices=TAX_YEAR, default=YEAR_2016)
    due_date = models.DateField()
    payment_date = models.DateField()
    deposit_form = models.FileField(upload_to='accounting/taxdues/',blank=True)
    details = RichTextField(blank=True)

    created_at = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'tax_filing'
        ordering = ['payment_date']


    def __str__(self):
        return u'taxpayment ' + str(self.id)

    def __unicode__(self):
        return u'taxpayment ' + str(self.id)

class QuartlyFiling(models.Model):
    tax_type = models.IntegerField(choices=TAX_TYPE, default=FEDERAL_TAXES_941_944)
    tax_period = models.IntegerField(choices=TAX_PERIOD, default=Q1)
    tax_year = models.IntegerField(choices=TAX_YEAR, default=YEAR_2016)
    due_date = models.DateField()
    filed_date = models.DateField()
    tax_form = models.FileField(upload_to='accounting/taxforms/',blank=True)
    details = RichTextField(blank=True)

    created_at = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'quartly_filing'
        ordering = ['filed_date']


    def __str__(self):
        return u'taxform ' + str(self.id)

    def __unicode__(self):
        return u'taxform ' + str(self.id)

from ecomstore.catalog.models import Brand
ORDERED = 1
PAID_BY_WIRE = 2
PAID_BY_PAYPAL = 3
PARTIALLY_SHIPPED = 4
ALL_SHIPPED = 5
ALL_DELIVERED = 6

ORDER_STATUS = ((ORDERED,'Order Placed'),
            (PAID_BY_WIRE,'Paid By Bank Wire Transfer'),
            (PAID_BY_PAYPAL,'Paid By Paypal'),
            (PARTIALLY_SHIPPED,'Partially Shipped'),
            (ALL_SHIPPED,'All Shipped'),
            (ALL_DELIVERED,'All Delivered'),)
class InventoryOrdering(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    status = models.IntegerField(choices=ORDER_STATUS, default=ORDERED)
    order_date = models.DateField()
    paid_date = models.DateField(blank=True)
    order_id = models.CharField(max_length=20)
    order_total = models.DecimalField(max_digits=9, decimal_places=2)
    pi = models.FileField(upload_to='accounting/inventoryordering/',blank=True)
    yet_to_receive = models.TextField()
    payment_receipt = RichTextField(blank=True)

    created_at = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'inventory_ordering'
        ordering = ['order_date']


    def __str__(self):
        return self.brand.name + self.order_id 

    def __unicode__(self):
        return self.brand.name + self.order_id 

    def all_trackings(self):
        return ', '.join([c.tracking_number for c in self.shipmenttracking_set.all()])
    all_trackings.short_description = "trackings"

EXPENSE_TYPE__OFFICESUPPLY = 1
EXPENSE_TYPE__AUTOMOBILE = 2
EXPENSE_TYPE__AIRLINETICKET = 3
EXPENSE_TYPE__HOTEL = 4
EXPENSE_TYPE__ITINFRASTRUCTURE = 5
EXPENSE_TYPE__BUSINESSMEAL = 6
EXPENSE_TYPE__CARRENTAL = 7
EXPENSE_TYPE__OTHER = 8

EXPENSE_TYPE = ((EXPENSE_TYPE__OFFICESUPPLY,'Office Supplies'),
            (EXPENSE_TYPE__AUTOMOBILE,'Automobile, Gas'),
            (EXPENSE_TYPE__AIRLINETICKET,'Business Travel - airline ticket'),
            (EXPENSE_TYPE__CARRENTAL,'Business Travel - car rental'),
            (EXPENSE_TYPE__HOTEL,'Business Travel - Hotel'),
            (EXPENSE_TYPE__ITINFRASTRUCTURE,'IT Infrastructure, Phone Communication'),
            (EXPENSE_TYPE__BUSINESSMEAL,'Business Meal'),
            (EXPENSE_TYPE__OTHER,'All Other Expenses'),)


class ExpenseBookkeeping(models.Model):
    #business_entity = models.ForeignKey(BusinessEntity, default=get_business_entity, on_delete=models.CASCADE)
    expense_type = models.IntegerField(choices=EXPENSE_TYPE, default=EXPENSE_TYPE__OFFICESUPPLY)
    category = models.CharField(max_length=30, null=True, blank=True)
    expense_date = models.DateField()
    expense_place = models.CharField(max_length=30, null=True, blank=True)
    expense_total = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    receipt = models.FileField(upload_to='accounting/expenses/',blank=True)
    details = RichTextField(blank=True)

    created_at = models.DateField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'bookkeeping_expense'
        ordering = ['expense_date']


    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return str(self.id) 


SHIPMENT_STATUS_SHIPPED = 1
SHIPMENT_STATUS_DELIVERED_DUTY_UNPAID = 2
SHIPMENT_STATUS_DELIVERED_DUTY_PAID = 3
SHIPMENT_STATUS = ((SHIPMENT_STATUS_SHIPPED,'Shipped, Intransit'),
            (SHIPMENT_STATUS_DELIVERED_DUTY_UNPAID,'Delivered, Duty Unpaid'),
            (SHIPMENT_STATUS_DELIVERED_DUTY_PAID,'Delivered, Duty Paid'),)

DUTY_PAYMENT_UNPAID = 0
DUTY_PAYMENT_COD = 1
DUTY_PAYMENT_ONLINE = 2
DUTY_PAYMENT_CHECK_MAIL = 3
DUTY_PAYMENT_CHECK_BILLPAYMENT = 4
DUTY_PAYMENT_TYPE = ((DUTY_PAYMENT_COD,'Duty Collected by driver'),
            (DUTY_PAYMENT_UNPAID,'Duty unpaid'),
            (DUTY_PAYMENT_ONLINE,'Duty Paid on their web site'),
            (DUTY_PAYMENT_CHECK_MAIL,'Duty Paid by Check Mailing'),
            (DUTY_PAYMENT_CHECK_BILLPAYMENT,'Duty Paid by Bank Bill Payment'),)


class ShipmentTracking(models.Model):
    tracking_number = models.CharField(max_length=30)
    order = models.ForeignKey(InventoryOrdering, on_delete=models.CASCADE)
    packing_list = models.FileField(upload_to='accounting/inventoryordering/',blank=True)
    status = models.IntegerField(choices=SHIPMENT_STATUS, default=SHIPMENT_STATUS_SHIPPED)
    duty_amount = models.DecimalField(max_digits=9, decimal_places=2, null=True,blank=True)
    payment_by = models.IntegerField(choices=DUTY_PAYMENT_TYPE, default=DUTY_PAYMENT_UNPAID)
    commercial_invoice = models.FileField(upload_to='accounting/inventoryordering/',blank=True)
    payment_stub = models.FileField(upload_to='accounting/inventoryordering/',blank=True)
    details = RichTextField(blank=True)

