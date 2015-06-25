import tarfile


def compress_module(file_list, output_file):
    with tarfile.open(output_file, "w:gz") as tf:
        for file_name in file_list:
            tf.add(file_name)
