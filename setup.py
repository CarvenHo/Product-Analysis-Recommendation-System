import pathlib

import setuptools

HERE = pathlib.Path(__file__).parent.resolve()
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding="utf-8")
setuptools.setup(
    name="ecomre",
    version="1.0.0",
    description="ecommerce recommendation",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Carven",
    packages=setuptools.find_namespace_packages(include=["capstone_iod.*"]),
    package_data={"": ["*.json"]},
    python_requires=">=3.9, <4",

)
