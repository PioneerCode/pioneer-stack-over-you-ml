"""Repository servicing Stack Overflow 2017 developer survey dataset."""
import pandas as pd


RESULTS_PATH = 'data/2017-results.csv'
SCHEMA_PATH = 'data/2017-schema.csv'

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
