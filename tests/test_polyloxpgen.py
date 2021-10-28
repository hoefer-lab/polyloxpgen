
### this requires pip install pytest
### if installed, run >>> pytest within the /tests directory

from ..polyloxpgen import polylox_pgen
from ..polylox_merge import *
from .. import polylox_pgen
import numpy as np
import pandas as pd

def test_single_sample_output_bc1020_ld2017():
    purged_barcodes_ref = np.loadtxt('bc1020_BarPipe.txt', usecols=0, skiprows=1, delimiter='\t', dtype=str)
    purged_reads_ref = np.loadtxt('bc1020_BarPipe.txt', usecols=1, skiprows=1, delimiter='\t')
    data_minrecs_ref = np.loadtxt('bc1020_BarPipe.txt', usecols=3, skiprows=1, delimiter='\t', dtype=int)
    data_pgen_ref = np.loadtxt('bc1020_BarPipe.txt', usecols=4, skiprows=1, delimiter='\t')

    print(purged_barcodes_ref)
    print(purged_reads_ref)
    print(data_minrecs_ref)
    print(data_pgen_ref)

    # TODO: finish test when outer loading part is done
    assert 2 == 3

def test_single_sample_output_bc1022_ld2017():
    purged_barcodes_ref = np.loadtxt('bc1022_BarPipe.txt', usecols=0, skiprows=1, delimiter='\t', dtype=str)
    purged_reads_ref = np.loadtxt('bc1022_BarPipe.txt', usecols=1, skiprows=1, delimiter='\t')
    data_minrecs_ref = np.loadtxt('bc1022_BarPipe.txt', usecols=3, skiprows=1, delimiter='\t', dtype=int)
    data_pgen_ref = np.loadtxt('bc1022_BarPipe.txt', usecols=4, skiprows=1, delimiter='\t')

    print(purged_barcodes_ref)
    print(purged_reads_ref)
    print(data_minrecs_ref)
    print(data_pgen_ref)

    # TODO: finish test when outer loading part is done
    assert 2 == 3

def test_two_sample_output():
    # TODO placeholder ...
    assert 2 == 2
