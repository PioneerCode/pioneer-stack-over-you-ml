#
#  Archived data (developer_survey_2017.zip) comes directly from Stack Overflow
#  https://insights.stackoverflow.com/survey/?utm_source=so-owned&utm_medium=blog&utm_campaign=dev-survey-2017&utm_content=blog-link&utm_term=data
#  https://drive.google.com/uc?export=download&id=0B6ZlG_Eygdj-c1kzcmUxN05VUXM
#
"""Repository servicing Stack Overflow 2017 developer survey dataset."""
import os
import zipfile
import pandas as pd

ARCHIVE_PATH = 'data/developer_survey_2017.zip'
RESULTS_PATH = 'data/unpacked/survey_results_public.csv'
SCHEMA_PATH = 'data/unpacked/survey_results_schema.csv'

FEATURE_COLUMNS = [
    'Professional',
    'ProgramHobby',
    'Country',
    'University',
    'FormalEducation',
    'MajorUndergrad',
    'YearsProgram',
    'YearsCodedJobPast'
]


def get_test_train_data(label_name='DeveloperType'):
    """Parses the csv file in RESULTS_PATH."""

    # Insure files are on disk
    maybe_unzip()

    # Parse the local CSV file.
    results = pd.read_csv(
        filepath_or_buffer=RESULTS_PATH,
        # names=CSV_COLUMN_NAMES,  # list of column names
        header=0  # ignore the first row of the CSV file.
    )

    (train, test) = split_data(results)

    # 1. Assign the DataFrame's labels (the right-most column) to results_label.
    # 2. Delete (pop) the labels from the DataFrame.
    # 3. Assign the remainder of the DataFrame to results_features
    train_features, train_label = train.loc[:, FEATURE_COLUMNS], train.pop(
        label_name)

    test_features, test_label = test.loc[:, FEATURE_COLUMNS], test.pop(
        label_name)

    return (train_features, train_label), (test_features, test_label)


def split_data(data_frame):
    """Split our results data in test and train"""
    train = data_frame.sample(frac=0.8, random_state=200)
    test = data_frame.drop(train.index)
    return (train, test)


def maybe_unzip():
    """Unpack Archive if not already unpacked"""
    if do_files_exist is not True:
        zip_ref = zipfile.ZipFile(ARCHIVE_PATH, 'r')
        zip_ref.extractall('data/unpacked')
        zip_ref.close()


def do_files_exist():
    """Check if files are on disk"""
    if os.path.isfile(RESULTS_PATH):
        return True

    return False
