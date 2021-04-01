import os
import pathlib
import sys
from shutil import rmtree

from setuptools import Command, find_packages, setup

__title__ = "fastapi_route_log"
__description__ = "A FastAPI route for logging every request " 
__url__ = "https://github.com/12345k/fastapi_logging.git"
__author_email__ = "karathickaravindan@gmail.com"
__license__ = "MIT"
__requires__ = ["fastapi","starlette","user_agents","pydantic" ]
__keywords__ = ["fastapi","logging","custom","router"]
__version__ = "0.0.4"
__author__ = "karthick aravindan (12345k)"

here = pathlib.Path(__file__).parent
about = {}

# # Load the package's _version.py module as a dictionary.
# with open(os.path.join(here, __title__, "_version.py")) as f:
#     exec(f.read(), about)

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


# __version__ = about["__version__"]


setup(
    name=__title__,
    version=__version__,
    description=__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=__url__,
    author=__author__, #about["__author__"],
    author_email=__author_email__,
    license=__license__,
    packages=find_packages(exclude=("test",)),
    keywords=__keywords__,
    install_requires=__requires__,
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
    ],

)
