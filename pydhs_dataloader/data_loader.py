# -*- coding: utf-8 -*-

"""Console script for pydhs_dataloader."""
import sys
import click
from pydhs_dataloader.pydhs_dataloader import Dataloader


def data_import(basedir, login, passwd):
    loader = Dataloader(basedir)
    loader.rename_all_zip_files_to_lowercase()
    loader.create_directories()
    loader.unzip_all_files()
    loader.rename_all_dta_files_to_lowercase()
    loader.write_csv_files_from_stata()
    loader.import_csvs_to_database()
    print('Data loaded to database. Refresh the database and check for completion.')


def clean(basedir):
    loader = Dataloader(basedir)
    loader.delete_csv_stata_directories()



if __name__ == "__main__":
    sys.exit(data_import())  # pragma: no cover
