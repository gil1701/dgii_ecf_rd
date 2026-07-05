from setuptools import setup, find_packages

with open("requirements.txt", encoding="utf-8") as f:
    install_requires = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="dgii_ecf_rd",
    version="0.0.1",
    description="Integración DGII e-CF para ERPNext en República Dominicana",
    author="Odalis Daniel Gutierrez Gil",
    author_email="",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
