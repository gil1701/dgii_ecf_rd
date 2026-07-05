# DGII e-CF RD

Versión corregida: 0.0.2

App Frappe/ERPNext para estructura base de integración con Comprobantes Fiscales Electrónicos (e-CF) de la DGII República Dominicana.

## Cambio importante en 0.0.2

Se eliminó la creación automática de campos en `Customer` porque tu sitio ya tiene una customización inválida en Customer: `custom_governorate` / etiqueta `Governorate`, tipo `Link`, sin `Options`. Al agregar cualquier campo nuevo a Customer, Frappe valida todo el DocType Customer y falla por ese campo existente.

La app ahora solo crea campos en `Sales Invoice` y usa `Customer.tax_id` como fuente inicial para RNC/Cédula.
