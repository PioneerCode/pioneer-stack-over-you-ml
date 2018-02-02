#
#  Archived data (developer_survey_2017.zip) comes directly from Stack Overflow
#  https://insights.stackoverflow.com/survey/?utm_source=so-owned&utm_medium=blog&utm_campaign=dev-survey-2017&utm_content=blog-link&utm_term=data
#  https://drive.google.com/uc?export=download&id=0B6ZlG_Eygdj-c1kzcmUxN05VUXM
#
"""Repository servicing Stack Overflow 2017 developer survey dataset."""
import os
import zipfile
import data_clean
import pandas as pd
import tensorflow as tf

ARCHIVE_PATH = 'data/developer_survey_2017.zip'
RESULTS_PATH = 'data/unpacked/survey_results_public.csv'
SCHEMA_PATH = 'data/unpacked/survey_results_schema.csv'
CLEAN_PATH = 'data/unpacked/cleaned/cleaned_survey_results_public.csv'
LABELS = ['Sentosa', 'Versicolor', 'Virginica']


def get_test_train_data():
    """Parses the csv file in RESULTS_PATH."""

    # TODO: If we already have a cleaned dataset, lets just return that
    # Insure files are on disk
    maybe_unzip()
    raw_data = None

    # Parse the local CSV file.
    if not os.path.isfile(CLEAN_PATH):
        raw_data = pd.read_csv(
            filepath_or_buffer=RESULTS_PATH,
            header=0,
            low_memory=False
        )
        output = data_clean.FEATURE_COLUMNS
        output.append(data_clean.LABEL_NAME)
        raw_data.loc[:, output].to_csv(CLEAN_PATH, index=False)
    else:
        raw_data = pd.read_csv(
            filepath_or_buffer=CLEAN_PATH,
            header=0,
            low_memory=False
        )

    return data_clean.get_clean_data(raw_data)


def maybe_unzip():
    """Unpack Archive if not already unpacked"""
    if os.path.isfile(RESULTS_PATH) is not True:
        zip_ref = zipfile.ZipFile(ARCHIVE_PATH, 'r')
        zip_ref.extractall('data/unpacked')
        zip_ref.close()

