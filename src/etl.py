'''
Convert the raw data, do some transformation, create train.csv and test.csv 
under data folder.

Usage:
    python3 src/etl.py
'''
import logging
from pathlib import Path
import click

import pandas as pd
import numpy as numpy
from sklearn.impute import SimpleImputer

@click.command()
@click.argument('config_file', type=str, default="src/config.yml")

def etl(config_file):
    

if __name__ == '__main__':
    etl()