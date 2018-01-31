"""Stack Overflow  DNNClassifier for the 2017 developer survey dataset."""
import pandas as pd

RESULTS_PATH = 'data/2017-results.csv'
SCHEMA_PATH = 'data/2017-schema.csv'

def load_data():
    """Parses the csv file in RESULTS_PATH."""

    # Parse the local CSV file.
    train = pd.read_csv(
        filepath_or_buffer=RESULTS_PATH,
        # names=CSV_COLUMN_NAMES,  # list of column names
        header=0  # ignore the first row of the CSV file.
    )

    return train


print(load_data())
