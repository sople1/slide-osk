=============================
Slide-OSK
=============================
 :copyright: (c) SnooeyNET
 :license: MIT

.. moduleauthor:: Seongsu Yoon <sople1@sitori.net>

Summary
=======

On Screen Keyboard with Slide

Installation
============

Commons
-------

You must install Python 3 and required pip packages.
In development, make virturlenv environment is good choice for you.


Windows
-------

1. Check if you installed Python 3.7.4 or upper
2. Clone this git repository and open it Command Prompt
4. If you want to make virtualenv, follow below command:

.. code-block:: bash

    # make virtualenv on env folder of repository folder
    > python3 -m venv env

    # run
    > env\Scripts\activate

5. install pip packages in requirements.txt

.. code-block:: bash

    > pip install -r requirements.txt

6. Launch by app.py

.. code-block:: bash

    > python app.py


macOS/Linux
-----------

1. Check if you installed Python 3.7.4 or upper
2. Clone this git repository and open it at Terminal
3. If you want to make virtualenv, follow below command:

.. code-block:: bash

    # make virtualenv on env directory of repository directory
    $ python3 -m venv ./env

    # run by bash shell
    $ source env/bin/activate

4. install pip packages in requirements.txt

.. code-block:: bash

    $ pip install -r requirements.txt

5. Launch by app.py

.. code-block:: bash

    $ python app.py


Documentation
=============

Commons
-------

This package using Sphinx for auto documentation.


Windows
-------

1. follow below command:

.. code-block:: bash

    # first run
    > env\Scripts\sphinx-quickstart.exe

2. after work - it skips what exist files, make seperated files

.. code-block:: bash

    > env\Scripts\sphinx-apidoc.exe -F -o docs . --separate

3. use command if you want to build html document

.. code-block:: bash

    > env\Scripts\sphinx-build.exe -b html docs docs/_build/html


macOS/Linux
-----------

1. follow below command:

.. code-block:: bash

    # first run
    $ ./env/bin/sphinx-quickstart

2. after work - it skips what exist files, make seperated files

.. code-block:: bash

    $ ./env/bin/sphinx-apidoc -F -o docs . --separate

3. use command if you want to build html document

.. code-block:: bash

    $ ./env/bin/sphinx-build -b html docs docs/_build/html


Configuration
=============

not yet


See also
========

not yet
