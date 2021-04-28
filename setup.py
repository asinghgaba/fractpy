import setuptools

exec(open("fractpy/version.py", "r").read())

# Read in the requirements.txt file
with open("requirements.txt") as f:
    requirements = []
    for library in f.read().splitlines():
        requirements.append(library)

# Read in the test_requirements.txt file
with open("tests/test_requirements.txt") as f:
    test_requirements = []
    for library in f.read().splitlines():
        test_requirements.append(library)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fractpy",
    version=__version__,
    install_requires=requirements,
    author="Amarjit Singh Gaba",
    author_email="asinghgaba@gmail.com",
    description="A library to generate fractals",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/asinghgaba/fractpy",
    project_urls={
        "Bug Tracker": "https://github.com/asinghgaba/fractpy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
    extras_require={
        "dev": test_requirements,
    },
)
