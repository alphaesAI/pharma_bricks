from src.etl.preprocessing.parser import EDIParser


def test_parser():
    parser = EDIParser()
    generic_json = parser.parse("samples/837_actual_data.txt")
    # print(generic_json)


if __name__ == "__main__":
    test_parser()