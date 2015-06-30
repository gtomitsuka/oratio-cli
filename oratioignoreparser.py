import os
import re


class OratioIgnoreParser():
    def __init__(self):
        self.ignored_paths = ["oratiomodule.tar.gz"]

    def load(self, oratio_ignore_path):
        with open(oratio_ignore_path, "r") as f:
            self.ignored_paths.extend([line.strip() for line in f])

    def extend_list(self, ignored_paths_list):
        self.ignored_paths.extend(ignored_paths_list)

    def should_be_ignored(self, filepath):
        filepath = filepath.replace("\\", "/")
        for ig in self.ignored_paths:
            compiled_regex = re.compile(
                '^' + re.escape(ig).replace('\\*', '.*') + '$'
            )
            if compiled_regex.search(filepath) or \
                    compiled_regex.search(filepath.split('/')[-1]):
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
