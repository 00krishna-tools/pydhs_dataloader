# -*- coding: utf-8 -*-

"""Main module."""

import os
import zipfile
import shutil
import tqdm
import pandas as pd
import subprocess

######################################
## Functions for extracting zip files
##
######################################
class Dataloader:
    def __init__(self, basedir):
        self.basedir = os.path(basedir)
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

    def unzip_all_files(self):
        list_zipfiles = list_files(self.basedir, 'zip')
        for f in tqdm(list_zipfiles):
            unzip_one_file(f, self.statadir)
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
            d = pd.read_stata(f)
            new_filename = os.path.join(self.csvdir, get_basename_of_file_without_extension(f)+'.csv')
            d.write_csv(new_filename, header=True, index=None)


######################################
## Functions for importing csv files to
## database
##
######################################

    def import_csvs_to_database(self, login, passwd):
        list_csvs = list_files(self.csvdir, 'csv')
        for f in tqdm(list_csvs):
            cmd = 'pgfutter --db "db_dhs" --port "5432" --schema "public" --user {} --pass {} --ignore-errors csv {} \;'
            subprocess.call(cmd.format(login, passwd, f))





def list_files(directory, extension):
    file_list = []
    for (dirpath, dirnames, filenames) in walk(directory):
        for f in filenames:
            if f.endswith('.' + extension):
                file_list.append(os.path.join(dirpath, f))
    return file_list

def get_basename_of_file_without_extension(file):
    return os.path.splitext(file)[0]
