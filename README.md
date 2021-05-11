# FractPy: a Python library for generating fractals

[![PyPI](https://img.shields.io/pypi/v/fractpy?color=blue)](https://pypi.org/project/fractpy/)
[![License: MIT](https://raw.githubusercontent.com/asinghgaba/fractpy/master/docs/_static/license.svg)](https://github.com/asinghgaba/fractpy/blob/master/LICENSE)
![](https://github.com/asinghgaba/fractpy/workflows/CI/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/fractpy/badge/?version=master)](https://fractpy.readthedocs.io/en/master/?badge=master)
[![codecov](https://codecov.io/gh/asinghgaba/fractpy/branch/master/graph/badge.svg?token=RZBB3MWH7Y)](https://codecov.io/gh/asinghgaba/fractpy)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This library currently implements the generation of following fractals:

- [Newton Fractal](https://en.wikipedia.org/wiki/Newton_fractal)
  - For Newton Fractal, this library can currently be used only for polynomial functions with real powers.

**FractPy** relies on `sympy`, `numpy`, and `matplotlib` - all part of the standard scientific Python stack so is easy to install on all operating systems.

## How do I install FractPy?

The recommended way to install `fractpy` is using Python Package index (PyPi), to install use the following command:

```bash
$ python -m pip install fractpy
```

## How do I use FractPy?

Here is an example of generating Newton Fractal for <img src="https://render.githubusercontent.com/render/math?math=f(x) = x^8 - 4x^3 %2B x^2 - 6">:

```python
from fractpy.models import NewtonFractal
model = NewtonFractal("x**8 - 4x**3 + x**2 - 6")
p = model.plot(-2, 2, -2, 2, (1000, 1000))
p.show()
```

The above code will generate the following plot:

![](https://raw.githubusercontent.com/asinghgaba/fractpy/master/docs/_static/readme_plot.png)

Full documentation is available here: https://fractpy.readthedocs.io/

## How can I contribute to FractPy?

After forking and cloning the forked repository on your computer, change the directory to fractpy and create a virtual environment:

```bash
$ cd fractpy
$ python -m venv env 
```

Activate the virtual environment and install tox:

```bash
$ . env/bin/activate
$ python -m pip install tox
```

Make the required changes and then run the tests using tox (Make sure to run the tests before opening a PR):

```bash
$ python -m tox
```


All contributions are welcome, whether it be adding new methods of generating fractals, writing documentation, or fixing embarrassing bugs!

In the interest of fostering an open and welcoming environment, all
contributors, maintainers and users are expected to abide by the Python code of
conduct: https://www.python.org/psf/codeofconduct/

## Getting Help

For more information or to ask questions about FractPy join our [Slack Channel](https://fractpy.slack.com.).

## Licensing

FractPy is fully open source. For more information about its license, see [LICENSE](https://github.com/asinghgaba/fractpy/blob/master/LICENSE).



