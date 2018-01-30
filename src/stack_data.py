import pandas as pd

RAW_DATA_PATH = 'data/2016.csv'


def load_data(label_name='Species'):
    """Returns Stack Overflow Developer survey dataset."""

    # Parse the local CSV file.
    train = pd.read_csv(
        filepath_or_buffer=RAW_DATA_PATH,
        # names=CSV_COLUMN_NAMES,  # list of column names
        header=0  # ignore the first row of the CSV file.
    )

    return train

print(load_data())
