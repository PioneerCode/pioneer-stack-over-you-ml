"""Stack Overflow  DNNClassifier for the 2017 developer survey dataset."""
import tensorflow as tf
import stack_data


def main():
    """Entry"""

    # Fetch the data
    (results_features, results_label) = stack_data.load_data()
    print(results_features)


main()
