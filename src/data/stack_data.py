import os
import pandas as pd
import zipfile

PARENT = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
ARCHIVE_FILE_PATH = os.path.join(
    PARENT, 'data', 'raw', 'developer_survey_2017.zip')
UNPACKED_PATH = os.path.join(PARENT, 'data', 'raw', 'unpacked')
RAW_FILE_PATH = os.path.join(UNPACKED_PATH, 'survey_results_public.csv')
CACHE_PATH = os.path.join(PARENT, 'data', 'raw', 'cache')
CACHE_FILE_PATH = os.path.join(CACHE_PATH, 'cached_survey_results_public.csv')

FEATURE_COLUMNS = [
    'Professional',
    'ProgramHobby',
    'Country',
    'University',
    'FormalEducation',
    'MajorUndergrad',
    'YearsProgram'
]
LABEL_NAME = 'DeveloperType'


def get_features_and_columns():
    '''
    Get list of features and label
    '''
    names = FEATURE_COLUMNS
    names.append(LABEL_NAME)
    return names


def maybe_unpack():
    '''
    Unpack Archive if not already unpacked
    '''
    if os.path.isfile(UNPACKED_PATH) is not True:
        zip_ref = zipfile.ZipFile(ARCHIVE_FILE_PATH, 'r')
        zip_ref.extractall(UNPACKED_PATH)
        zip_ref.close()


def load_data():
    '''
    Get raw data based on features and label list
    '''
    if not os.path.isfile(CACHE_FILE_PATH):
        print(RAW_FILE_PATH)

        raw_data = pd.read_csv(RAW_FILE_PATH,
                               header=0,
                               low_memory=False
                               )
        raw_data = raw_data.loc[:, get_features_and_columns()]
        raw_data = raw_data.to_csv(
            CACHE_FILE_PATH, index=False)
    else:
        raw_data = pd.read_csv(CACHE_FILE_PATH,
                               low_memory=False)

    return raw_data


def get_data():
    '''
    Get raw dataframe of 2017 data
    '''
    # Create cache directory
    if not os.path.exists(CACHE_PATH):
        os.makedirs(CACHE_PATH)

    maybe_unpack()
    return load_data()


get_data()
