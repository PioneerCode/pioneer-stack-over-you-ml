'''a'''
import pandas as pd
from sklearn import preprocessing


def remove_multi_label(raw_data, label_name):
    # Iterate all rows and drop ones with MultiLabel, effectively
    # turning this into a MultiClass problem.
    expanded_data = []
    for (idx, row) in raw_data.iterrows():
        # Check for delimiter
        split = [x.strip() for x in row.loc[label_name].split(';')]
        if len(split) is 1:
            expanded_data.append(row)

    return pd.DataFrame(expanded_data).reset_index(drop=True)


def remove_unlabeled(raw_data, label_name):
    '''Remove all rows with no label values'''
    return raw_data.dropna(subset=[label_name], how='all')


def label_encode(df, columns):
    for col in columns:
        le = preprocessing.LabelEncoder()
        col_values_unique = list(df[col].unique())
        le_fitted = le.fit(col_values_unique)

        col_values = list(df[col].values)
        le.classes_
        col_values_transformed = le.transform(col_values)
        df[col] = col_values_transformed
    return df


def get_encoded(raw_data, label_name):

    unlabeled_data = remove_unlabeled(raw_data, label_name)
    single_label_data = remove_multi_label(unlabeled_data, label_name)
    to_be_encoded_cols = single_label_data.columns.values
    return label_encode(single_label_data, to_be_encoded_cols)
