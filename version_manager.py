# -*- coding: utf-8 -*-

class CheckRepo(object):
    def check_repository(self):
        print 'soy un colaborador ou yeah'
        return 'soy un colaborador'

class VersionManager(object):

    def __init__(self, check_repo=None):
        self.check_repo = check_repo

    def check_file(self, repo, requirements):
        if self.check_repo:
            self.check_repo.check_repository()
        return '{} has no outdated packages'.format(repo)
