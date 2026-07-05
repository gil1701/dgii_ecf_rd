app_name = "dgii_ecf_rd"
app_title = "DGII e-CF RD"
app_publisher = "Odalis Daniel Gutierrez Gil"
app_description = "Integración DGII e-CF para ERPNext República Dominicana"
app_email = ""
app_license = "MIT"
app_version = "0.0.1"

# Includes in Desk
# app_include_js = "/assets/dgii_ecf_rd/js/dgii_ecf_rd.js"
# app_include_css = "/assets/dgii_ecf_rd/css/dgii_ecf_rd.css"

# Installation hooks
after_install = "dgii_ecf_rd.install.after_install"

# Document events. These are intentionally conservative so installation does not break.
doc_events = {
    "Sales Invoice": {
        "on_submit": "dgii_ecf_rd.api.on_sales_invoice_submit"
    }
}

# Fixtures can be added later when custom fields/workflows are finalized.
fixtures = []
