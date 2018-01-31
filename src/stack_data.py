"""Stack Overflow  DNNClassifier for the 2017 developer survey dataset."""
import pandas as pd

RESULTS_PATH = 'data/2017-results.csv'
SCHEMA_PATH = 'data/2017-schema.csv'

CSV_COLUMN_NAMES = [
    'Professional',
    'ProgramHobby',
    'Country',
    'University',
    'FormalEducation',
    'MajorUndergrad',
    'YearsProgram',
    'YearsCodedJobPast',
    'DeveloperType'
]


def load_data(label_name='DeveloperType'):
    """Parses the csv file in RESULTS_PATH."""

    # Parse the local CSV file.
    results = pd.read_csv(
        filepath_or_buffer=RESULTS_PATH,
        names=CSV_COLUMN_NAMES,  # list of column names
        header=0  # ignore the first row of the CSV file.
    )

    # 1. Assign the DataFrame's labels (the right-most column) to results_label.
    # 2. Delete (pop) the labels from the DataFrame.
    # 3. Assign the remainder of the DataFrame to results_features
    results_features, results_label = results, results.pop(label_name)

    return (results_features, results_label)


print(load_data())
