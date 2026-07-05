import frappe


def on_sales_invoice_submit(doc, method=None):
    """Placeholder hook for e-CF generation/submission.

    This function is deliberately non-destructive. It marks that the app hook was
    reached, but does not send documents to DGII until credentials, XML mapping,
    certificate handling, and environment endpoints are fully configured.
    """
    try:
        if hasattr(doc, "dgii_ecf_status") and not doc.dgii_ecf_status:
            frappe.db.set_value(doc.doctype, doc.name, "dgii_ecf_status", "Pendiente de envío")
    except Exception:
        frappe.log_error(frappe.get_traceback(), "DGII e-CF RD on_submit")


@frappe.whitelist()
def ping():
    return {"ok": True, "app": "dgii_ecf_rd"}
