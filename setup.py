import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ChordalPy",
    version="0.1.0",
    author="P-bibs",
    author_email="author@example.com",
    description="Parse and manipulate musical chords",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/P-bibs/ChordalPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)