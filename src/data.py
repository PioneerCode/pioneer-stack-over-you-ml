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
CLEAN_PATH = 'data/unpacked/cleaned_survey_results_public.csv'
LABEL_NAME = 'DeveloperType'
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


def get_test_train_data():
    """Parses the csv file in RESULTS_PATH."""

    # TODO: If we already have a cleaned dataset, lets just return that
    # Insure files are on disk
    maybe_unzip()

    # Parse the local CSV file.
    results = get_dataframe_from_csv()
    results.loc[:, FEATURE_COLUMNS].to_csv(CLEAN_PATH, index=False)
    (train, test) = split_data_into_test_train(results)
    return split_data_into_feature_label(train, test)


def maybe_unzip():
    """Unpack Archive if not already unpacked"""
    if do_archived_files_exist is not True:
        zip_ref = zipfile.ZipFile(ARCHIVE_PATH, 'r')
        zip_ref.extractall('data/unpacked')
        zip_ref.close()


def get_dataframe_from_csv():
    """Load data into dataframe"""
    return pd.read_csv(
        filepath_or_buffer=RESULTS_PATH,
        header=0,  # ignore the first row of the CSV file.
        low_memory=False
    )


def split_data_into_test_train(data_frame):
    """Split our results data in test and train"""
    train = data_frame.sample(frac=0.8, random_state=200)
    test = data_frame.drop(train.index)
    return (train, test)


def split_data_into_feature_label(train, test):
    """Split train test data into feature label sets"""
    # 1. Assign the DataFrame's labels (the right-most column) to {}_label.
    # 2. Delete (pop) the labels from the DataFrame.
    # 3. Assign the remainder of the DataFrame to {}_features
    train_features, train_label = train.loc[:, FEATURE_COLUMNS], train.pop(
        LABEL_NAME)

    test_features, test_label = test.loc[:, FEATURE_COLUMNS], test.pop(
        LABEL_NAME)

    return (train_features, train_label), (test_features, test_label)


def do_archived_files_exist():
    """Check if files are on disk"""
    if os.path.isfile(RESULTS_PATH):
        return True

    return False
