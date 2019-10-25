import sys


from .calculate import is_hash_match
from .parse import parse


def main():
    if len(sys.argv) < 2:
        print("please enter filename")
        return
    file_path = sys.argv[1]
    path_to_given_files = ""
    if len(sys.argv) > 2:
        path_to_given_files = sys.argv[2]
    try:
        with open(file_path) as f:
            content = f.readlines()
    except:
        print("file not found")
        return
    files = parse(content, path_to_given_files)
    for one_file in files:
        result = is_hash_match(one_file.path, one_file.alg, one_file.hash)
        print(f"{one_file.name} {result}")


if __name__ == "__main__":
    main()
