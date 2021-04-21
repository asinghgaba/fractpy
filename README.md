# FractPy: a python library for generating fractals

This library currently implements the generation of following fractals:

- [Newton Fractal](https://en.wikipedia.org/wiki/Newton_fractal)
  - For Newton Fractal, this library can currently be used only for polynomial functions with real powers.

**FractPy** relies on `sympy`, `numpy`, and `matplotlib` - all part of the standard scientific Python stack so is easy to install on all operating systems.

## How do I install FractPy?

The recommended way to install `fractpy` is using Python Package index (PyPi), to install use the following command:

```bash
$ pip install fractpy
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

![](https://github.com/asinghgaba/fractpy/blob/master/docs/_static/readme_plot.png)

Full documentation is available here: https://fractpy.readthedocs.io/

## How can I contribute to FractPy?

To install development version of this library:

```bash
$ python setup.py develop
```

All contributions are welcome, whether it be adding new methods of generating fractals, writing documentation, or fixing embarrassing bugs!

In the interest of fostering an open and welcoming environment, all
contributors, maintainers and users are expected to abide by the Python code of
conduct: https://www.python.org/psf/codeofconduct/

## Getting Help

For more information or to ask questions about FractPy join our [Slack Channel](https://fractpy.slack.com.).

## Licensing

FractPy is fully open source. For more information about its license, see [LICENSE](https://github.com/asinghgaba/fractpy/blob/master/LICENSE).



