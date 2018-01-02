# -*- coding: utf-8 -*-

class CheckRepo:
    def check_repository(self):
        # we must check the repository...
        pass
class VersionManager:

    def __init__(self, check_repo=None):
        self.check_repo = check_repo

    def check_file(self, requirements):
        if not requirements:
            return 'this project has no package list'
        if self.check_repo:
            self.check_repo.check_repository()
