import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():

    frappe.delete_doc("Custom Field", "Purchase Invoice-etr_serial_number", force=True)
    frappe.delete_doc("Custom Field", "Purchase Invoice-etr_column_break", force=True)
    frappe.delete_doc("Custom Field", "Purchase Invoice-etr_invoice_number", force=True)

    custom_fields = {
        "Purchase Invoice": [
            {
                "fieldname": "etr_data",
                "label": "ETR Data",
                "fieldtype": "Tab Break",
                "insert_after": "supplied_items",
                "allow_on_submit": True,
                "translatable": 1
            },
            {
                "fieldname": "etr_invoice_number",
                "label": "ETR Invoice Number",
                "fieldtype": "Data",
                "collapsible": 0,
                "insert_after": "etr_data",
                "allow_on_submit": True,
                "translatable": 1
            }
        ]
    }

    create_custom_fields(custom_fields)