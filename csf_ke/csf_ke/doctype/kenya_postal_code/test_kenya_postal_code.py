# Copyright (c) 2026, Navari Ltd and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestKenyaPostalCode(FrappeTestCase):
	def test_postal_code_creation(self) -> None:
		"""Test that a Kenya Postal Code can be created with required fields."""
		if frappe.db.exists("Kenya Postal Code", "99999"):
			frappe.delete_doc("Kenya Postal Code", "99999", force=True)

		doc = frappe.get_doc(
			{
				"doctype": "Kenya Postal Code",
				"postal_code": "99999",
				"town": "Test Town",
				"country": "Kenya",
			}
		)
		doc.insert(ignore_permissions=True)
		self.assertTrue(doc.name)
		self.assertEqual(doc.name, "99999")
		self.assertEqual(doc.town, "Test Town")
