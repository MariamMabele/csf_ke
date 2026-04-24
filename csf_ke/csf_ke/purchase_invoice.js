frappe.ui.form.on("Purchase Invoice", {
	supplier: function(frm) {
		if (!frm.doc.supplier) {
			return;
		}

		frappe.db.get_value("Supplier", frm.doc.supplier, "withholding_vat_rate").then((r) => {
			frm.set_value("withholding_vat_rate", flt(r.message.withholding_vat_rate || 0));
			frm.trigger("set_withholding_vat_amount");
		});
	},

	validate: function(frm) {
		frm.trigger("set_withholding_vat_amount");
	},

	set_withholding_vat_amount: function(frm) {
		frm.set_value(
			"withholding_vat_amount",
			flt(frm.doc.net_total) * flt(frm.doc.withholding_vat_rate) / 100
		);
	},
});
