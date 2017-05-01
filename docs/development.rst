Developing marshmallow_configparser
===================================

Prepare development environment
-------------------------------

Create new virtual environment

.. code-block:: sh

    cd path/to/cloned/repo/marshmallow_configparser
    pyvenv .venv
    source .venv/bin/activate

Then ensure we have newest pip and setuptools

.. code-block:: sh

    pip install -U pip
    wget https://bootstrap.pypa.io/ez_setup.py -O - | python

To be able to package project into wheels, we need

.. code-block:: sh

    pip install wheel

And to distribute it on PyPI_

.. code-block:: sh

    pip install twine


Install it in develop mode
--------------------------

.. code-block:: sh

    python setup.py develop

Later, to uninstall it

.. code-block:: sh

    python setup.py develop --uninstall

To install extra packages usefull in development

.. code-block:: sh

    pip install -e .[dev]


Running tests
-------------

.. code-block:: sh

    python setup.py test -a "tests"

or to get more verbose output

.. code-block:: sh

    python setup.py test -a "--spec tests"

or to generate tests coverage

.. code-block:: sh

    py.test --cov=marshmallow_configparser --cov-report=html tests/

and finally, tests can be run with tox_

.. code-block:: sh

    tox


Runing under PyPy3
------------------

.. code-block:: sh

    wget https://bitbucket.org/pypy/pypy/downloads/pypy3.3-v5.5.0-alpha-linux64.tar.bz2
    tar xvfj pypy3.3-v5.5.0-alpha-linux64.tar.bz2
    virtualenv -p /foo/bar/baz/pypy3-v5.5.0-linux64/bin/pypy3pypy3 .venvpypy
    source .venvpypy/bin/python


Profiling
---------

Use IPython shell to generate profiling data

.. code-block:: python

    %prun -D program.prof [mover.move(d) for d in moves_cycle]

After that, it is viewable by either Snakeviz

.. code-block:: sh

    snakeviz program.prof

or as call graph through KCacheGrind

.. code-block:: sh

    pyprof2calltree -i program.prof
    kcachegrind program.prof.log


Uploading to PyPI
-----------------

.. code-block:: sh

    pip install -U twine

Prepare ``~/.pypirc``

.. code-block:: ini

    [distutils]
    index-servers=
        pypi
        pypitest

    [pypitest]
    repository = https://testpypi.python.org/pypi
    username = <username>
    password = <password>

    [pypi]
    repository = https://pypi.python.org/pypi
    username = <username>
    password = <password>

Create dist

.. code-block:: sh

    python setup.py sdist bdist_wheel

An upload it

.. code-block:: sh

    twine upload -r pypitest dist/*

.. _PyPI: https://pypi.python.org/pypi
.. _tox: https://tox.readthedocs.io/en/latest/
