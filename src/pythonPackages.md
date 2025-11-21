Python Packages
====================
There are other ways to structure Python packages, but this is how I like to do it.  I'm using the `src/` layout, a package-root tests folder, and `setup.cfg` (primarily) for as much compatibility as I can manage.  I'm also assuming you're using Git and intend for other people to use the package.

File Structure
--------------------
A Python package should have its own directory with the same name as the package, containing:

``` verbatim
path/to/mypackage/
├── src/mypackage/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── tests/
│   ├── test_module1.py
│   └── test_module2.py
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
├── setup.cfg
└── setup.py
```

The actual package code is stored in `src/mypackage/`, splitting into separate modules (.py files) as-needed for organizational purposes.  It's possible to have sub-packages within your package, but I don't generally bother with that and if you're reading this tutorial you probably shouldn't either.

You'll notice I've added ``__init__.py``.  This is how you specify what is made available when the package is imported.  It should look like this:
```python
from .module1 import foo
from .module2 import bar

__all__ = ["foo", "bar"]

```
You first decide what objects you'd like to import by default from your package.  Then, you import them locally (that's what the dot means: look in this package directory) and write their names into the `__all__` list.  Yes, it really is their names as strings and not the objects themselves.  The example above would let you do `import pypackage` and then use `mypackage.foo` and `mypackage.bar`.

Setup System
--------------------
Python has not one but three files you can use to define the package setup system, due to the community finding fault in the previous approaches.  Hopefully they'll stop now.  The systems are:

1. `setup.py` the original approach to packaging.  The idea was that you could run `python setup.py` and it would install the package.  It fell out of favor because it was difficult to figure out what the package contained without installing it.
2. `setup.cfg` was the attempt to make a declarative approach to package installation, so that the system could read e.g. dependencies, version numbers, etc. without having to run the script.  Nearly all Python installations these days support it.
3. `pyproject.toml` is the modern Python installation method, which uses a more standardized `.toml` format and integrates well with outside tools (testers, linters, etc.).  Python has supported it for a while now, but many system-installed Python versions still predate it as of 2025.

You'll see my example includes all three.  The "real" one is `setup.cfg`, I've included dummy versions the other two that redirect all their definitions back to `setup.cfg` for maximum compatibility with other Python versions.  For `setup.py` that's just:
``` python
import setuptools

if __name__ == "__main__":
    setuptools.setup()
```
and for `pyproject.toml`:
``` toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
```

For the *actual* setup data, here's how you'd lay out your `setup.cfg` file
``` ini
[metadata]
name = mypackage
version = 1.1
author = Johnny Fakename
author_email = fakename@example.com
description = A Python package that definitely does something.

[options]
packages = mypackage
package_dir =
    =src
install_requires =
    setuptools ; python_version > "3.11"
    numpy
    scipy
```
You'll need to fill in the info specific to your package, but the fields are pretty self-explanatory.  The exceptions are probably "package_dir" which is just how you let it know you're using the `src` layout, and "install_requires", which defines the packages your package needs to work.  There's an [elaborate syntax](https://packaging.python.org/en/latest/specifications/dependency-specifiers/#dependency-specifiers) that lets you specify *exactly* what version of a package you need, even letting you vary it by Python version.  This example requires `setuptools` only if the version of Python being used is 3.11 or higher (because this is last version before the alternative `distutils` was deprecated).  You don't necessarily need `numpy` and `scipy`, I just threw those in as an example.

Once that is all ready, you can install your package from its directory with `pip install .`.

Tests
--------------------
If you're doing anything even remotely complicated, it can be *extremely* helpful to write tests as you go.  You'll almost certainly have to write some kind of tests as you develop the code, so by organizing them properly you can catch if something you do breaks code that previously worked.  These days the way to do testing in Python is with [Pytest](https://docs.pytest.org/en/stable/).  In the recommended file structure, I left a `test` directory with test file in it, each corresponding to a .py file in `src`.  That's just my preference though; if you're not going to do a ton of tests, you could instead just put one test module in the root directory.  Pytest will find tests automatically based on the function and file names: start them both with "test_" (though there are other options).  A basic test module might look like this:
```python
import numpy as np
from pytest import approx, raises
from mypackage import somefunction

def test_somefunction():
    # Check the function against a known value
    assert somefunction(2.5) == approx(np.sin(2.5) * 3)
    # Randomly generate some test cases
    for i in range(100):
        xt = 10*np.random.randn()
        # Verifying that somefunction is odd (for example)
        assert somefunction(xt) == approx(-somefunction(-xt))
    # Check that it raises an exception for an infinite input
    with raises(ValueError):
        somefunction(np.inf)
```

Pytest has a pretty wide range of ways you can test things (faking files to use as test cases, reading print() outputs, etc), but even a simple handful of assertions can be very helpful.  In this example I've used two especially common methods.  [`pytest.approx`](https://docs.pytest.org/en/stable/reference.html#pytest-approx) allows the assertion to pass even if the values differ very slightly (common for floating point numbers).  The other one is [`pytest.raises`](https://docs.pytest.org/en/stable/reference.html#pytest-raises), which only passes the test if the code inside the `with` statement *does* raise the given exception.  You can use this to make sure your error reporting and edge cases are working as expected.

Assuming you've installed Pytest, you should just be able to run `pytest` from your package root directory and it will run all the tests it finds and let you know if any of the tests failed.  If so, it will tell you what the values were if the assertion was a comparison.  If you're familiar with the Python debugger [pdb](https://docs.python.org/3/library/pdb.html), you can run `pytest --pdb` to have it attach directly at any failed assertion so you can figure out what happened.

Other Files
--------------------
1. The Readme.md file is a nice way to store basic information about the package: installation, usage, notes, and so on.  If you're using Github, this will be rendered on the repository's home page.  If you aren't using Github, the only real advantages is that the [markdown syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) is fairly convenient and it's a file other people may be used to looking for.
2. The license file is required so that other people can legally use your code.  Admittedly, some people ignore this (especially AI companies looking for data to train on), but that doesn't mean we should encourage such things.  Apparently, the legal issues can get *weird* if you have multiple contributors but no license.  I am not a lawyer and you probably aren't either, so you should just use an existing well-established license.  Github can suggest some based on your needs, or [see here](https://choosealicense.com/).
3. The .gitignore file tells git which files it can ignore for version tracking purposes.  This can be helpful for not worrying about random setup byproducts or Python cache files.  The documentation is [here](https://git-scm.com/docs/gitignore) but at it's core it's just a list of patterns to ignore, with a * as a wildcard.  When you make a repository with Github, you can use their [default Python .gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore) to start you off.

Further Reading
--------------------
1. [Setuptools documentation](https://setuptools.pypa.io/en/latest/setuptools.html)
2. [Pytest Documentation](https://docs.pytest.org/en/stable/)
3. [Cython Compilation Guide](https://cython.readthedocs.io/en/stable/src/userguide/source_files_and_compilation.html)
