import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="np_chaonay", # Replace with your own username
    version="1.0.4",
    author="Nuttapong Punpipat",
    author_email="nuttapongpunpipat@gmail.com",
    description="Objects collection package by NP-chaonay",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NP-chaonay/PythonPkg-np_chaonay",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
