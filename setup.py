import setuptools
from directory2docker import Version


setuptools.setup(
    name="directory2ocker",
    version=Version("1.0.0").number,
    description="Python Package Boilerplate",
    long_description=open("README.rst").read().strip(),
    author="Sachin Chandra",
    author_email="sachin@netbook.ai",
    py_modules=["directory2docker"],
    install_requires=[],
    license="MIT License",
    zip_safe=False,
    keywords="boilerplate package",
    classifiers=["Packages", "Boilerplate"],
)
