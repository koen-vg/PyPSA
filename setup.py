# -*- coding: utf-8 -*-
from __future__ import absolute_import

from codecs import open

from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pypsa",
    version="0.21.2",
    author="PyPSA Developers, see https://pypsa.readthedocs.io/en/latest/developers.html",
    author_email="t.brown@tu-berlin.de",
    description="Python for Power Systems Analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PyPSA/PyPSA",
    license="MIT",
    packages=find_packages(exclude=["doc", "test"]),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "scipy",
        "pandas>=0.24.0",
        "xarray",
        "netcdf4",
        "tables",
        "pyomo>=5.7",
        "linopy>=0.0.13, <0.1",
        "matplotlib",
        "networkx>=1.10",
        "deprecation",
    ],
    extras_require={
        "dev": ["pytest", "pypower", "pandapower", "scikit-learn"],
        "cartopy": ["cartopy>=0.16"],
        "docs": [
            "numpydoc",
            "sphinx",
            "sphinx_rtd_theme",
            "nbsphinx",
            "nbsphinx-link",
            "black",
            "scikit-learn",
        ],
        "gurobipy": ["gurobipy"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
)
