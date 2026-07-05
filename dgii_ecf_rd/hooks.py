app_name = "dgii_ecf_rd"
app_title = "DGII e-CF RD"
app_publisher = "Odalis Daniel Gutierrez Gil"
app_description = "Integración DGII e-CF para ERPNext República Dominicana"
app_email = ""
app_license = "MIT"
app_version = "0.0.2"

after_install = "dgii_ecf_rd.install.after_install"

doc_events = {
    "Sales Invoice": {
        "on_submit": "dgii_ecf_rd.api.on_sales_invoice_submit"
    }
}

fixtures = []
