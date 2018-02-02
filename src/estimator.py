"""Stack Overflow  DNNClassifier for the 2017 developer survey dataset."""
import data


def main():
    """Entry"""
    # Fetch the data
    (train_feature, train_label), (test_feature, test_label) = data.get_test_train_data()
    print("Training Features Shape: {0}".format(train_feature.shape))
    print("Training Label Shape: {0}".format(train_label.shape))
    print("Test Features Shape: {0}".format(test_feature.shape))
    print("Test Label Shape: {0}".format(test_label.shape))

main()
