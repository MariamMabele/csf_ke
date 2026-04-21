from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
	custom_fields = {
		"Landed Cost Item": [
			{
				"fieldname": "applicable_charges_per_item",
				"fieldtype": "Currency",
				"insert_after": "applicable_charges",
				"label": "Applicable Charges per Item",
				"read_only": 1,
			},
			{
				"fieldname": "price_per_item",
				"fieldtype": "Currency",
				"insert_after": "applicable_charges_per_item",
				"label": "Price per Item",
				"read_only": 1,
			},
		]
	}

	create_custom_fields(custom_fields, update=True)
