## polyloxpgen

Barcode purging and pgen (probability of generation) calculation for Polylox data.

##### Methods

polyloxpgen contains two main methods
- polylox_merge: merge samples from multiple raw barcode files ([RPBPBR](https://github.com/hoefer-lab/RPBPBR) output)
- polylox_pgen: purge barcodes and compute pgen for single or multiple samples

##### Docs/Workflow example

please visit the example.ipynb jupyter notebook for a workflow example and some
further notes

##### TODO

unclear how to output the data, as txt file?
barcode with "" before and after? if not we should note that people
have to be careful with excel as it might render barcode as dates etc.

##### Note

these scripts are based on the original [polylox (MATLAB)](https://github.com/hoefer-lab/polylox) implementation;

see there also for more information
