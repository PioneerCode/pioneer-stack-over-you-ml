"""Transform raw data into clean dataframe."""
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

LABEL_NAME = 'DeveloperType'


def get_clean_data(raw_data):
    """Get clean dataframe"""
    (train, test) = split_data_into_test_train(raw_data)
    return split_data_into_feature_label(train, test)


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
