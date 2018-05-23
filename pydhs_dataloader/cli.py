# -*- coding: utf-8 -*-

"""Console script for pydhs_dataloader."""
import sys
import click
from pydhs_dataloader.pydhs_dataloader import Dataloader



@click.command()
@click.argument('basedir', type=click.Path(exists=True))
@click.argument('login')
@click.argument('passwd')
def import(basedir, login, passwd):

    loader = Dataloader(basedir)
    loader.create_directories()
    loader.unzip_all_files()
    loader.write_csv_files_from_stata()
    loader.import_csvs_to_database(login, passwd)
    print('Data loaded to database. Refresh the database and check for completion.')

@click.command()
@click.argument('basedir', type=click.Path(exists=True))
def clean(basedir):
    loader = Dataloader(basedir)
    loader.delete_csv_stata_directories()



if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
