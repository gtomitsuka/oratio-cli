import tarfile
import os

from oratioignoreparser import OratioIgnoreParser


def compress_files(file_list, output_file):
    with tarfile.open(output_file, "w:gz") as tf:
        for file_name in file_list:
            tf.add(file_name)


def compress_module(directory):
    parser = OratioIgnoreParser()
    oi = os.path.join(directory, ".oratio-ignore")
    if os.path.isfile(oi):
        parser.load(oi)
    compress_files(parser.list_files(".")[0], "oratiomodule.tar.gz")
