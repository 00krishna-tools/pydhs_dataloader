# -*- coding: utf-8 -*-

"""Main module."""

import os
import zipfile
import shutil
from tqdm import tqdm
import pandas as pd
import subprocess
from pathlib import Path

######################################
## Functions for extracting zip files
##
######################################
class Dataloader:
    def __init__(self, basedir):
        self.basedir = basedir
        self.csvdir = os.path.join(self.basedir, 'csvfiles/')
        self.statadir = os.path.join(self.basedir, 'stata/')

    def create_directories(self):

        if not os.path.exists(self.statadir):
            os.mkdir(self.statadir)
        if not os.path.exists(self.csvdir):
            os.mkdir(self.csvdir)
        print('New directories created')
        return 0

    def delete_csv_stata_directories(self):

        if os.path.exists(self.statadir):
            shutil.rmtree(self.statadir)
        if os.path.exists(self.csvdir):
            shutil.rmtree(self.csvdir)
        print('csv and stata directories removed.')

    def rename_all_zip_files_to_lowercase(self):
        filenames = os.listdir(self.basedir)
        for filename in filenames:
            os.rename(os.path.join(self.basedir, filename), os.path.join(self.basedir, filename.lower()))

    def rename_all_dta_files_to_lowercase(self):
        filenames = os.listdir(self.statadir)
        for filename in filenames:
            os.rename(os.path.join(self.statadir, filename), os.path.join(self.statadir, filename.lower()))

    def unzip_all_files(self):
        list_zipfiles = list_files(self.basedir, 'zip')
        for f in tqdm(list_zipfiles):
            self.unzip_one_file(f)
        print('All zip files successfully extracted.')

    def unzip_one_file(self, pathtofile):
        zip_ref = zipfile.ZipFile(pathtofile, 'r')
        zip_ref.extractall(self.statadir)
        zip_ref.close()

######################################
## Functions for converting stata to csv
##
######################################

    def write_csv_files_from_stata(self):
        list_statafiles = list_files(self.statadir, 'dta')
        for f in tqdm(list_statafiles):
            d = pd.read_stata(f, convert_categoricals=False)
            new_filename = os.path.join(self.csvdir, get_basename_of_file_without_extension(f)+'.csv')
            d.to_csv(new_filename.lower(), header=True, index=None)


######################################
## Functions for importing csv files to
## database
##
######################################

    def import_csvs_to_database(self):
        cmd = './import_tables {}'
        cmd = cmd.format(self.csvdir)
        subprocess.call(cmd)





def list_files(directory, extension):
    file_list = []
    for (dirpath, dirnames, filenames) in os.walk(directory):
        for f in filenames:
            if f.endswith('.' + extension):
                file_list.append(os.path.join(dirpath, f))
    return file_list

def get_basename_of_file_without_extension(file):
    return os.path.splitext(Path(file).name)[0].lower()
