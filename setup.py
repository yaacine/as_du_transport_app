from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in as_du_transport/__init__.py
from as_du_transport import __version__ as version

setup(
	name="as_du_transport",
	version=version,
	description="app to manage asDuTransport doctypes",
	author="yacine",
	author_email="yacine.zidel@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
