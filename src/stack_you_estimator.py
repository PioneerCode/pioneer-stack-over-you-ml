"""Stack Overflow  DNNClassifier for the 2017 developer survey dataset."""
import stack_data


def main():
    """Entry"""

    # Fetch the data
    (train_feature, train_label), (test_feature, test_label) = stack_data.get_test_train_data()
    print(train_feature.shape)
    print(test_feature.shape)

main()
