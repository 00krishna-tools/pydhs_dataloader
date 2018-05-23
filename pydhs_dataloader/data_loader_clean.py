# -*- coding: utf-8 -*-

"""Console script for pydhs_dataloader."""

import sys
import click
from pydhs_dataloader.pydhs_dataloader import Dataloader

@click.command()
@click.argument('basedir', type=click.Path(exists=True))
def clean(basedir):
    loader = Dataloader(basedir)
    loader.delete_csv_stata_directories()

if __name__ == "__main__":
    sys.exit(clean())  # pragma: no cover
