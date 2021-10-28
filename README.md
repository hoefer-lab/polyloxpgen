## polyloxpgen

Barcode purging and pgen (probability of generation) calculation for Polylox data.

#### ***Methods***

polyloxpgen contains two main methods
- polylox_merge: merge samples from multiple raw barcode files ([RPBPBR](https://github.com/hoefer-lab/RPBPBR) output)
- polylox_pgen: purge barcodes and compute pgen for single or multiple samples

#### ***Installation***

to use polyloxpgen and the above methods, install it via

```
pip install polyloxpgen
```

#### ***Docs/Workflow example***

please visit the example.ipynb jupyter notebook for a workflow example and some
further notes

#### ***References / Final notes***

- these scripts are based on the original [polylox (MATLAB)](https://github.com/hoefer-lab/polylox) implementation; see there also for more information
- original publication: [Pei et al., Nature, 2017](https://www.nature.com/articles/nature23653)
