import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def after_install():
    """Create only Sales Invoice fields.

    We intentionally do not touch Customer here. If a site has an unrelated
    invalid Customer custom field, adding a new Customer field forces Frappe to
    validate Customer meta and installation fails.
    """
    custom_fields = {
        "Sales Invoice": [
            {"fieldname": "dgii_ecf_section", "label": "DGII e-CF", "fieldtype": "Section Break", "insert_after": "taxes_and_charges", "collapsible": 1},
            {"fieldname": "dgii_ecf_ncf", "label": "NCF / e-NCF", "fieldtype": "Data", "insert_after": "dgii_ecf_section", "read_only": 0},
            {"fieldname": "dgii_ecf_status", "label": "Estado DGII", "fieldtype": "Data", "insert_after": "dgii_ecf_ncf", "read_only": 1},
            {"fieldname": "dgii_ecf_track_id", "label": "Track ID DGII", "fieldtype": "Data", "insert_after": "dgii_ecf_status", "read_only": 1},
        ]
    }
    create_custom_fields(custom_fields, update=True, ignore_validate=True)
    frappe.db.commit()
