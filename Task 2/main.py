import hashlib

hash_file = "hash_file.txt"


def get_data(hash_file_address):
    """
    reads the file that passes as the parameter. Splits the lines into the lists,
    then appends lists to the empty list
    :param hash_file_address:
    :return: list of lists based on lines in file
    """
    data_hash_from_file = []
    try:
        with open(hash_file_address) as file:
            read_file = file.readlines()
            for line in read_file:
                data_hash_from_file.append(line.split())
        return data_hash_from_file
    except FileNotFoundError:
        print(f"{hash_file_address} - file not found")
        return 0


def compare_hash(data_hash):
    """
    compares hash code from the file with the actual hash code of that file.
    :param data_hash:
    :return:
    """
    for i in range(len(data_hash)):
        try:
            with open(data_hash[i][0], "rb") as file_opened:
                read_file = file_opened.read()

                if data_hash[i][1] == "MD5":
                    md5_hash = hashlib.md5(read_file)
                    md5_hashed = md5_hash.hexdigest()
                    if data_hash[i][2] == md5_hashed:
                        print(f"{data_hash[i][0]} OK")
                    else:
                        print(f"{data_hash[i][0]} FAIL")
                elif data_hash[i][1] == "SHA1":
                    sha1_hash = hashlib.sha1(read_file)
                    sha1_hashed = sha1_hash.hexdigest()
                    if data_hash[i][2] == sha1_hashed:
                        print(f"{data_hash[i][0]} OK")
                    else:
                        print(f"{data_hash[i][0]} FAIL")
                elif data_hash[i][1] == "SHA256":
                    sha256_hash = hashlib.sha256(read_file)
                    sha256_hashed = sha256_hash.hexdigest()
                    if data_hash[i][2] == sha256_hashed:
                        print(f"{data_hash[i][0]} OK")
                    else:
                        print(f"{data_hash[i][0]} FAIL")
        except FileNotFoundError:
            print(f"{data_hash[i][0]} NOT FOUND")


def main():
    try:
        compare_hash(get_data(hash_file))
    except TypeError:
        pass


if __name__ == "__main__":
    main()
else:
    print("You cannot use this program as a module")



