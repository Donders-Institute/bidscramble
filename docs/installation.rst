Installation
============

The BIDScramble software runs on multiple platforms (e.g. Linux, MacOS,
Windows) that have a Python 3.10+ installation.

It is recommended (but not required) to first create a virtual
environment.

.. code-block:: console

   python -m venv venv
   source venv/bin/activate

You can then install the BIDScramble tools using git and pip.

.. code-block:: console

   git clone https://github.com/Donders-Institute/BIDScramble.git
   pip install ./BIDScramble           # Or use an alternative installer
   pip install ./BIDScramble[fif]      # Use this if you have fif data
   pip install -e ./BIDScramble[dev]   # Recommended for developers only
