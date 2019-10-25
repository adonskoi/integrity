"""module for parse content"""

import collections

File = collections.namedtuple("File", "name path alg hash")


def parse(content, path_to_files):
    """
    params: 
        content - list of string "name algorithm given_hash"
        path_to_files - path to dir with files
    return:
        list of namedtuple("File", "name path alg hash")
    """
    files = []
    if path_to_files and path_to_files.strip()[-1] != "/":
        path_to_files += "/"
    for line in content:
        line = line.split()
        files.append(File(line[0], path_to_files + line[0], line[1], line[2]))
    return files
