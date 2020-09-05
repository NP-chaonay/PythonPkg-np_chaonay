import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="np_chaonay",
    version="1.3.0.dev",
    author="Nuttapong Punpipat",
    author_email="nuttapongpunpipat@gmail.com",
    description="Objects collection package by NP-chaonay",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NP-chaonay/PythonPkg-np_chaonay",
    packages=setuptools.find_packages(),
    classifiers=[
        "Topic :: Other/Nonlisted Topic",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    python_requires='>=3.0',
)
