
.. image:: https://img.shields.io/pypi/v/polyloxpgen.svg
    :target: https://pypi.python.org/pypi/polyloxpgen
    :alt: Latest PyPI version

.. image:: https://travis-ci.com/mauricelanghinrichs/polyloxpgen.svg?branch=master
   :target: https://travis-ci.com/mauricelanghinrichs/polyloxpgen
   :alt: Latest Travis CI build status

.. image:: https://codecov.io/gh/mauricelanghinrichs/polyloxpgen/branch/master/graph/badge.svg?token=MUWGE04ERH
   :target: https://codecov.io/gh/mauricelanghinrichs/polyloxpgen

TODO: adapt badges to polyloxpgen

polyloxpgen
^^^^^^^^^^^

Barcode purging and pgen (probability of generation) calculation for Polylox data.


**Methods**

polyloxpgen contains two main methods

- polylox_merge: merge samples from multiple raw barcode files (`RPBPBR <https://github.com/hoefer-lab/RPBPBR>`_ output)

- polylox_pgen: purge barcodes and compute pgen for single or multiple samples


**Installation**

to use polyloxpgen and the above methods, install it via

   pip install polyloxpgen


**Docs / Workflow example**

please visit the example.ipynb jupyter notebook for a workflow example and some
further notes (in the examples folder)


**References / Final notes**

- these scripts are based on the original `polylox (MATLAB) <https://github.com/hoefer-lab/polylox>`_ implementation; see there also for more information

- original publication: `Pei et al., Nature, 2017 <https://www.nature.com/articles/nature23653>`_
