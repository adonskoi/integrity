"""
module for check file hash with given hash value

"""
import hashlib


def calculate_file_hash(f, alg, buf_size):
    """BUF_SIZE - 64 kb
    need for large file"""
    h = hashlib.new(alg)
    for chunk in iter(lambda: f.read(buf_size), b""):
        h.update(chunk)
    return h.hexdigest()


def check_alg(alg):
    if alg not in {"md5", "sha1", "sha256"}:
        return False
    return True


def is_hash_match(filepath, alg, hash, buf_size=65536):
    """ Calculate file hash and compare with given.
    params:
        filepath - path to file 
        alg - hash algorithm, correct values: 'md5', 'sha1', 'sha256'
        hash - given file hash to compare with
        buf_size - bufer size for calculate hash, default 64kb
    return: 
        'OK' - hash match
        'FAIL' - hash not match
        'NOT FOUND' - file not found
        'WRONG ALG' - algorithm does not support
    """
    if not check_alg(alg):
        return "WRONG ALG"
    result = ""
    try:
        f = open(filepath, "rb")
    except:
        result = "NOT FOUND"
    else:
        calc_hash = calculate_file_hash(f, alg, buf_size)
        f.close()
        if calc_hash == hash:
            result = "OK"
        else:
            result = "FAIL"
    return result
