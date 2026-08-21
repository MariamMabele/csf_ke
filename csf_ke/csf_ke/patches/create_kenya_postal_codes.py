import json
import os

import frappe


def execute():
	"""One-time import of Kenya Postal Codes from bundled JSON fixture."""
	base_path = frappe.get_module_path("csf_ke")
	json_file_path = os.path.join(
		base_path, "patches", "kenya_postal_code_data.json"
	)

	if not os.path.exists(json_file_path):
		frappe.log_error(
			"Kenya Postal Code data file not found at: " + json_file_path,
			"Patch Error",
		)
		return

	with open(json_file_path) as f:
		data = json.load(f)

	records = data.get("records", data) if isinstance(data, dict) else data

	existing_codes: set[str] = set(
		frappe.get_all("Kenya Postal Code", pluck="name")
	)

	inserted = 0
	for record in records:
		postal_code = record.get("postal_code", "")
		if postal_code in existing_codes:
			continue

		frappe.get_doc(
			{
				"doctype": "Kenya Postal Code",
				"postal_code": postal_code,
				"town": record.get("town", ""),
				"county": record.get("county"),
				"region": record.get("region"),
				"postal_region_code": record.get("postal_region_code", ""),
				"country": record.get("country", "Kenya"),
				"source_url": record.get("source_url", ""),
			}
		).insert(ignore_permissions=True)
		inserted += 1

		if inserted % 100 == 0:
			frappe.db.commit()

	if inserted:
		frappe.db.commit()
		frappe.logger().info(
			f"Kenya Postal Codes patch: inserted {inserted} records"
		)
