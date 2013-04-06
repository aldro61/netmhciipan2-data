"""
NetMHCIIpan-2.0 [1] Dataset Downloader
Author: Alexandre Drouin

How to use:
    * Run this script with python to get a fresh copy of the NetMHCIIpan-2.0 dataset in the current directory.
        python netmhciipan_data.py

[1] Nielsen, Morten, et al. "NetMHCIIpan-2.0-Improved pan-specific HLA-DR predictions using a novel concurrent
    alignment and weight optimization training procedure." Immunome research 6.1 (2010): 9.
"""
import requests
import os
import shutil
from termcolor import *

def delete_directory_recursively(path):
    if os.path.isdir(path):
        shutil.rmtree(path)

cv_train_data_url = 'http://www.cbs.dtu.dk/suppl/immunology/NetMHCIIpan-2.0/Train/'
cv_train_folds = ['f000', 'f001', 'f002', 'f003', 'f004']
cv_test_folds = ['c000', 'c001', 'c002', 'c003', 'c004']
cv_download_dir = 'train'


ligand_test_data_url = 'http://www.cbs.dtu.dk/suppl/immunology/NetMHCIIpan-2.0/SYF/'
ligand_test_download_dir = 'test/ligands'

epitope_test_data_url = 'http://www.cbs.dtu.dk/suppl/immunology/NetMHCIIpan-2.0/IEDB/'
epitope_test_download_dir = 'test/epitopes'

print colored("Downloading training data", 'green')
print "*"*50
delete_directory_recursively(cv_download_dir)
os.makedirs(cv_download_dir)
for file in cv_train_folds:
    output_file_name = 'fold'+file[1:]+'_train.dat'
    print colored("File: " + file + ' -> ' + output_file_name, 'magenta')
    data = requests.get(os.path.join(cv_train_data_url, file))
    f = open(os.path.join(cv_download_dir, output_file_name), 'w')
    f.writelines(data.content)
    f.close()

for file in cv_test_folds:
    output_file_name = 'fold'+file[1:]+'_test.dat'
    print colored("File: " + file + ' -> ' + output_file_name, 'magenta')
    data = requests.get(os.path.join(cv_train_data_url, file))
    f = open(os.path.join(cv_download_dir, output_file_name), 'w')
    f.writelines(data.content)
    f.close()
print

print colored("Downloading testing dataset 1: Ligands from the SYFPEITHI database", 'green')
print "*"*50
delete_directory_recursively(ligand_test_download_dir)
os.makedirs(ligand_test_download_dir)
file = 'SYF.fsa'
output_file_name = 'syfpeithi_ligand_testing_set.fasta'
print colored("File: " + file + ' -> ' + output_file_name, 'magenta')
data = requests.get(os.path.join(ligand_test_data_url, file))
f = open(os.path.join(ligand_test_download_dir, output_file_name), 'w')
f.writelines(data.content)
f.close()
print

print colored("Downloading testing dataset 2: Epitopes from the IEDB database", 'green')
print "*"*50
delete_directory_recursively(epitope_test_download_dir)
os.makedirs(epitope_test_download_dir)
file = 'IEDB.fsa'
output_file_name = 'iedb_epitope_testing_set.fasta'
print colored("File: " + file + ' -> ' + output_file_name, 'magenta')
data = requests.get(os.path.join(epitope_test_data_url, file))
f = open(os.path.join(epitope_test_download_dir, output_file_name), 'w')
f.writelines(data.content)
f.close()
print
print colored('Download complete.', 'cyan')
