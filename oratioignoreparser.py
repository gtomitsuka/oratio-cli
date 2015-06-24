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
