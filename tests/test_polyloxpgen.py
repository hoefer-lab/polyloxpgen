
### this requires pip install pytest
### if installed, run >>> pytest within the /tests directory

import polyloxpgen.merge
import polyloxpgen.pgen
import numpy as np
import pandas as pd
import os

def test_single_sample_output_bc1020_ld2017():
    floc = os.path.join(os.path.dirname(__file__), '')

    ref_file = floc + 'original/bc1020_BarPipe.txt'
    purged_barcodes_ref = np.loadtxt(ref_file, usecols=0, skiprows=1, delimiter='\t', dtype=str)
    purged_reads_ref = np.loadtxt(ref_file, usecols=1, skiprows=1, delimiter='\t')
    data_minrecs_ref = np.loadtxt(ref_file, usecols=3, skiprows=1, delimiter='\t', dtype=int)
    data_pgen_ref = np.loadtxt(ref_file, usecols=4, skiprows=1, delimiter='\t')

    # run polylox_merge
    df_merged = polyloxpgen.merge.polylox_merge([floc + 'original/bc1020.barcode.count.txt'],
                                    ['bc1020'], floc + 'temp/', 'bc1020_merged')

    # run polylox_pgen
    df_pgen = polyloxpgen.pgen.polylox_pgen(floc + 'temp/bc1020_merged.txt',
                                        floc + 'temp/', 'bc1020_pgen',
                                        path_matrix_type='ld_2017')

    # read back from resulted file (corresponds to df_pgen)
    df_res = pd.read_csv(floc + 'temp/bc1020_pgen.txt', sep='\t', index_col=0)

    # delete temporary files in the end
    if os.path.isfile(floc + 'temp/bc1020_merged.txt'):
        os.remove(floc + 'temp/bc1020_merged.txt')
    if os.path.isfile(floc + 'temp/bc1020_pgen.txt'):
        os.remove(floc + 'temp/bc1020_pgen.txt')

    # check if the same set of barcodes comes out
    assert set(purged_barcodes_ref)==set(df_res.index.to_numpy(dtype=str))

    # then reindex to get the barcode order the same
    df_res = df_res.reindex(purged_barcodes_ref)

    # all remaining checks on the reorder df_res
    assert np.all(purged_barcodes_ref==df_res.index.to_numpy(dtype=str))
    assert np.all(purged_reads_ref==df_res.bc1020)
    assert np.all(data_minrecs_ref==df_res.MinRec)
    assert np.allclose(data_pgen_ref, df_res.Pgen)

def test_single_sample_output_bc1022_ld2017():
    floc = os.path.join(os.path.dirname(__file__), '')

    purged_barcodes_ref = np.loadtxt(floc + 'original/bc1022_BarPipe.txt', usecols=0, skiprows=1, delimiter='\t', dtype=str)
    purged_reads_ref = np.loadtxt(floc + 'original/bc1022_BarPipe.txt', usecols=1, skiprows=1, delimiter='\t')
    data_minrecs_ref = np.loadtxt(floc + 'original/bc1022_BarPipe.txt', usecols=3, skiprows=1, delimiter='\t', dtype=int)
    data_pgen_ref = np.loadtxt(floc + 'original/bc1022_BarPipe.txt', usecols=4, skiprows=1, delimiter='\t')

    # run polylox_merge
    df_merged = polyloxpgen.merge.polylox_merge([floc + 'original/bc1022.barcode.count.txt'],
                                    ['bc1022'], floc + 'temp/', 'bc1022_merged')

    # run polylox_pgen
    df_pgen = polyloxpgen.pgen.polylox_pgen(floc + 'temp/bc1022_merged.txt',
                                        floc + 'temp/', 'bc1022_pgen',
                                        path_matrix_type='ld_2017')

    # read back from resulted file (corresponds to df_pgen)
    df_res = pd.read_csv(floc + 'temp/bc1022_pgen.txt', sep='\t', index_col=0)

    # delete temporary files in the end
    if os.path.isfile(floc + 'temp/bc1022_merged.txt'):
        os.remove(floc + 'temp/bc1022_merged.txt')
    if os.path.isfile(floc + 'temp/bc1022_pgen.txt'):
        os.remove(floc + 'temp/bc1022_pgen.txt')

    # check if the same set of barcodes comes out
    assert set(purged_barcodes_ref)==set(df_res.index.to_numpy(dtype=str))

    # then reindex to get the barcode order the same
    df_res = df_res.reindex(purged_barcodes_ref)

    # all remaining checks on the reorder df_res
    assert np.all(purged_barcodes_ref==df_res.index.to_numpy(dtype=str))
    assert np.all(purged_reads_ref==df_res.bc1022)
    assert np.all(data_minrecs_ref==df_res.MinRec)
    assert np.allclose(data_pgen_ref, df_res.Pgen)

def test_two_sample_output_bc1020_bc1022_uniform():
    floc = os.path.join(os.path.dirname(__file__), '')

    # load reference dataframes
    df_merged_ref = pd.read_csv(floc + 'original/bc1020_bc1022_merged.txt', sep='\t', index_col=0)
    df_pgen_ref = pd.read_csv(floc + 'original/bc1020_bc1022_pgen_uniform.txt', sep='\t', index_col=0)

    # run polylox_merge
    df_merged = polyloxpgen.merge.polylox_merge([floc + 'original/bc1020.barcode.count.txt',
                                                floc + 'original/bc1022.barcode.count.txt'],
                                    ['bc1020', 'bc1022'], floc + 'temp/', 'bc1020_bc1022_merged')

    # run polylox_pgen
    df_pgen = polyloxpgen.pgen.polylox_pgen(floc + 'temp/bc1020_bc1022_merged.txt',
                                        floc + 'temp/', 'bc1020_bc1022_pgen',
                                        path_matrix_type='uniform')

    # read back from resulted files (correspond to df_merged and df_pgen)
    df_merged_res = pd.read_csv(floc + 'temp/bc1020_bc1022_merged.txt', sep='\t', index_col=0)
    df_pgen_res = pd.read_csv(floc + 'temp/bc1020_bc1022_pgen.txt', sep='\t', index_col=0)

    # delete temporary files in the end
    if os.path.isfile(floc + 'temp/bc1020_bc1022_merged.txt'):
        os.remove(floc + 'temp/bc1020_bc1022_merged.txt')
    if os.path.isfile(floc + 'temp/bc1020_bc1022_pgen.txt'):
        os.remove(floc + 'temp/bc1020_bc1022_pgen.txt')

    # compare merge dataframes
    assert np.all(df_merged_ref.index.to_numpy(dtype=str)==df_merged_res.index.to_numpy(dtype=str))
    assert np.all(df_merged_ref.bc1020==df_merged_res.bc1020)
    assert np.all(df_merged_ref.bc1022==df_merged_res.bc1022)

    # compare pgen dataframes
    assert np.all(df_pgen_ref.index.to_numpy(dtype=str)==df_pgen_res.index.to_numpy(dtype=str))
    assert np.all(df_pgen_ref.bc1020==df_pgen_res.bc1020)
    assert np.all(df_pgen_ref.bc1022==df_pgen_res.bc1022)
    assert np.all(df_pgen_ref.MinRec==df_pgen_res.MinRec)
    assert np.allclose(df_pgen_ref.Pgen, df_pgen_res.Pgen)
