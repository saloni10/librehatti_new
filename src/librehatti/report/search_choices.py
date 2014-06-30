CLIENT_FIELD_CHOICES = (
		('name', 'Name'),
    ('city', 'Address'),
	  ('phone', 'Phone'),('company','Company'),
	  )
	  
CLIENT_ORDER_CHOICES=(('name','Buyer'),('item','Item'),
		('quantity','Quantity'),('city', 'Customer City'),
		('unit price','Unit Price'),('discount','Discount')
		,('debit','Debit'),('total price','Total Price'),
		)
		
CLIENT_ORDER_TYPES_CHOICES=(
		('is_debit','Debit'),
		
)

CONSTRAINT_CHOICES= (
    ('date', 'Date'),
    ('gt','Amount greater than'),
    ('lt','Amount lesser than'),
)

