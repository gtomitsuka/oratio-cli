import os
import re


class OratioIgnoreParser():
    def __init__(self):
        self.ignored_paths = ["oratiomodule.tar.gz"]

    def load(self, oratio_ignore_path):
        with open(oratio_ignore_path, "r") as f:
            for line in f:
                self.ignored_paths.append(line.strip())

    def should_be_ignored(self, filepath):
        for ig in self.ignored_paths:
            if re.compile(re.escape(ig).replace('\\*', '.*')).search(filepath):
                return True
        return False

    def list_files(self, directory):
        filepaths = []
        ignored_files = []
        for root, dirs, files in os.walk("."):
            for name in files:
                relative_path = os.path.join(root, name)
                if relative_path.startswith("./"):
                    relative_path = relative_path[2:]
                if not self.should_be_ignored(relative_path):
                    filepaths.append(relative_path)
                else:
                    ignored_files.append(relative_path)
        return filepaths, ignored_files
