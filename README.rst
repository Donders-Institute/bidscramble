===========
BIDScramble
===========

|PyPI version| |BIDS| |GPLv3| |RTD| |Tests|

.. raw:: html

   <img name="bidscramble-logo" src="https://github.com/Donders-Institute/bidscramble/blob/main/docs/_static/bidscramble_logo.png" height="140px" alt=" ">

**BIDScramble** is a versatile tool that generates scrambled or **pseudo-random** `BIDS <https://bids-specification.readthedocs.io>`__ datasets from existing BIDS-structured data. It carefully preserves the statistical distributions of user-specified variables while maintaining the effects of interest, ensuring that the synthetic data remains analytically useful. Crucially, the output contains no or minimal indirect personal data, making it privacy-compliant and untraceable to original subjects.

This tool enables researchers to safely explore, prototype, and **test their analysis pipelines** on realistic yet anonymized data. Since the scrambled datasets retain key statistical properties, pipelines should behave similarly to how they would on real data — accelerating development without compromising privacy.

* Explore the full documentation on `Read the Docs <https://bidscramble.readthedocs.io>`__
* Access the open-source code on `GitHub <https://github.com/Donders-Institute/bidscramble>`__ (licensed under `GPL-3.0-or-later <https://spdx.org/licenses/GPL-3.0-or-later.html>`__)

Funding and acknowledgments
---------------------------

BIDScramble is being developed at the `Donders Institute <https://www.ru.nl/donders/>`__ of the `Radboud University <https://www.ru.nl>`__ as part of the `EOSC SIESTA <https://eosc-siesta.eu/>`__ project. Funding was received from the European Union’s Horizon Research and Innovation program under Grant agreement No. `101131957 <https://cordis.europa.eu/project/id/101131957>`__.

.. image:: https://raw.githubusercontent.com/SIESTA-eu/.github/main/profile/EN-Funded.jpg
   :height: 40px
   :alt: EU Funded Logo
   :target: https://cordis.europa.eu/project/id/101131957

.. image:: https://raw.githubusercontent.com/SIESTA-eu/.github/main/profile/logo.png
   :height: 40px
   :alt: EOSC SIESTA
   :target: https://eosc-siesta.eu/

Related tools
-------------

- https://github.com/PennLINC/CuBIDS
- https://peerherholz.github.io/BIDSonym
- https://arx.deidentifier.org
- https://github.com/SIESTA-eu/DatLeak
- https://github.com/SIESTA-eu/anjana
- https://github.com/IFCA-Advanced-Computing/pycanon

.. |PyPI version| image:: https://img.shields.io/pypi/v/bidscramble?color=success
   :target: https://pypi.org/project/bidscramble
   :alt: BIDScramble
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/bidscramble.svg
   :alt: Python 3
.. |GPLv3| image:: https://img.shields.io/badge/License-GPLv3+-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0
   :alt: GPL-v3.0 license
.. |RTD| image:: https://readthedocs.org/projects/bidscramble/badge/?version=latest
   :target: https://bidscramble.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation status
.. |BIDS| image:: https://img.shields.io/badge/BIDS-v1.10.0-blue
   :target: https://bids-specification.readthedocs.io/en/v1.10.0/
   :alt: Brain Imaging Data Structure (BIDS)
.. |Tests| image:: https://github.com/Donders-Institute/bidscramble/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/Donders-Institute/bidscramble/actions
   :alt: Pytest results
