import setuptools

exec(open("fractpy/version.py", "r").read())

requirements = ["numpy", "sympy", "matplotlib"]

setuptools.setup(
    name="fractpy", 
    version=__version__,
    requirements=requirements,
    author="Amarjit Singh Gaba",
    author_email="asinghgaba@gmail.com",
    description="A library to generate fractals",
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
)