import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-test-split", type=float, default=0.2) 

    args, _ = parser.parse_known_args()
    split_ration = args.train_test_split
    print(split_ration)