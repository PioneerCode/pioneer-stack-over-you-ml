import os
import pandas as pd
import zipfile

ARCHIVE_PATH = 'data/developer_survey_2017.zip'
RESULTS_PATH = 'data/unpacked/survey_results_public.csv'
CACHE_PATH = 'data/cache'
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


def maybe_unpack():
    # Unpack Archive if not already unpacked
    if os.path.isfile(RESULTS_PATH) is not True:
        zip_ref = zipfile.ZipFile(ARCHIVE_PATH, 'r')
        zip_ref.extractall('data/unpacked')
        zip_ref.close()

def load_data():
    # Builds column collection
    names = FEATURE_COLUMNS
    names.append(LABEL_NAME)

    # load data
    if not os.path.isfile('data/cache/cached_survey_results_public.csv'):
        raw_data = pd.read_csv(
            'data/unpacked/survey_results_public.csv',
            header=0,
            low_memory=False
        )
        raw_data = raw_data.loc[:, names]
        raw_data = raw_data.to_csv('data/cache/cached_survey_results_public.csv', index=False)
    else:
        raw_data = pd.read_csv('data/cache/cached_survey_results_public.csv', 
                            low_memory=False)

    return raw_data

def get_data():
    if not os.path.exists(CACHE_PATH):
        os.makedirs(CACHE_PATH)

    maybe_unpack()
    return load_data()


get_data()

