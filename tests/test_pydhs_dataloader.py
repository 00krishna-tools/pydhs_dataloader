#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pydhs_dataloader` package."""

import pytest

from click.testing import CliRunner

from pydhs_dataloader.data_loader import data_import
from pydhs_dataloader.data_loader_clean import clean


def test_data_loader():
    data_import('/media/rudra/sandbox/testing_pydhs_dataloader/', 'krishnab', '3kl4vx71')
