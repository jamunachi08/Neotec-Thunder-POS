from setuptools import setup, find_packages

setup(
    name="neotec_fnb",
    version="0.3.0",
    description="Neotec Thunder POS for ERPNext v15+",
    author="Neotec",
    author_email="support@neotec.ai",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
