from setuptools import setup, find_packages
setup(
    name='DAX_UTIL',
    version='0.0.0.25',
    author='Almir J Gomes',
    author_email='almir.jg@hotmail.com',
    packages=find_packages(),
    install_requires=[
        "python-dateutil>=2.9"
    ],
    python_requeries=">=3.9",
    description="Biblioteca de funcionalidades",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)