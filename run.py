from blueprint_reader import read_blueprint
import argparse


def run() -> None:
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file', type=argparse.FileType('rb'))

    args = arg_parser.parse_args()

    print(read_blueprint(args.file))

    args.file.close()


if __name__ == '__main__':
    run()
