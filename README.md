# DGII e-CF RD

App Frappe/ERPNext para estructura base de integración con Comprobantes Fiscales Electrónicos (e-CF) de la DGII República Dominicana.

## Corrección aplicada

Este ZIP incluye la estructura estándar esperada por `bench get-app` / `bench install-app`:

- `setup.py` en la raíz
- `requirements.txt`
- `MANIFEST.in`
- paquete Python `dgii_ecf_rd/`
- `hooks.py`
- `modules.txt`
- `patches.txt`
- módulo interno `dgii_ecf_rd/dgii_ecf_rd/doctype/...`

## Instalación

Desde el contenedor o servidor donde corre bench:

```bash
cd ~/frappe-bench
rm -rf apps/dgii_ecf_rd
unzip /ruta/dgii_ecf_rd_corrected.zip -d apps
mv apps/dgii_ecf_rd_corrected apps/dgii_ecf_rd
bench setup requirements
bench --site TU_SITIO install-app dgii_ecf_rd
bench --site TU_SITIO migrate
bench clear-cache
bench restart
```

Si quieres subirlo a GitHub:

```bash
cd ~/frappe-bench/apps/dgii_ecf_rd
git init
git add .
git commit -m "Fix Frappe app structure"
git branch -M main
git remote add origin https://github.com/gil1701/dgii_ecf_rd.git
git push -u origin main --force
```

Luego podrás instalarlo con:

```bash
bench get-app https://github.com/gil1701/dgii_ecf_rd.git
bench --site TU_SITIO install-app dgii_ecf_rd
```
