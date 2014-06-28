CLIENT_FIELD_CHOICES = (
		('user__username', 'Name'),
    ('address__city', 'Address'),
	  ('telephone', 'Phone'),
	  ('date_joined','Date of Joining'),('company','Company'),
	  )
	  
CLIENT_ORDER_CHOICES=(('item__name','Item'),('item__category','Category'),
		('qty','Quantity'),
		('item__price','Unit Price'),('discount','Discount')
		,('purchase_order__is_debit','Debit'),
		)
		
CLIENT_ORDER_TYPES_CHOICES=(
		('is_debit','Debit'),
		
)

