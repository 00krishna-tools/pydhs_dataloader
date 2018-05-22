# -*- coding: utf-8 -*-

"""Main module."""

import os
import zipfile
import shutil
import tqdm
import pandas as pd


######################################
## Functions for extracting zip files
##
######################################
def create_directories(basedir):
    statadir = os.path.join(basedir, 'stata/')
    csvdir = os.path.join(basedir, 'csvfiles/')
    if not os.path.exists(statadir):
        os.mkdir(statadir)
    if not os.path.exists(csvdir):
        os.mkdir(csvdir)
    print('New directories created')

    return 0

def delete_csv_stata_directories(basedir):
    statadir = os.path.join(basedir, 'stata/')
    csvdir = os.path.join(basedir, 'csvfiles/')
    if os.path.exists(statadir):
        shutil.rmtree(statadir)
    if os.path.exists(csvdir):
        shutil.rmtree(csvdir)
    print('csv and stata directories removed.')

def unzip_all_files(zipdir, statadir):
    list_zipfiles = list_files(zipdir, 'zip')
    for f in tqdm(list_zipfiles):
        unzip_one_file(f, statadir)
    print('All zip files successfully extracted.')

def unzip_one_file(pathtofile, targetdirectory)
    zip_ref = zipfile.ZipFile(pathtofile, 'r')
    zip_ref.extractall(targetdirectory)
    zip_ref.close()

######################################
## Functions for converting stata to csv
##
######################################

def write_csv_files_from_stata(statadirectory, csvdirectory):
    list_statafiles = list_files(statadirectory, 'dta')
    for f in tqdm(list_statafiles):
        d = pd.read_stata(f)
        new_filename = os.path.join(csvdirectory, get_basename_of_file_without_extension(f)+'.csv')
        d.write_csv(new_filename, header=True, index=None)


######################################
## Functions for importing csv files to
## database
##
######################################






def list_files(directory, extension):
    file_list = []
    for (dirpath, dirnames, filenames) in walk(directory):
        for f in filenames:
            if f.endswith('.' + extension):
                file_list.append(os.path.join(dirpath, f))
    return file_list

def get_basename_of_file_without_extension(file):
    return os.path.splitext(file)[0]
