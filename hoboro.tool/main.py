import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="shizuoka.csv")
    parser.add_argument("--fields", nargs="+")

    args = parser.parse_args()
    print(args.output)
    print(args.fields)


if __name__ == "__main__":
    main()
