# -*- coding: utf-8 -*-

class Colaborador(object):
    def algo_que_debe_llamarse(self):
        print 'soy un colaborador ou yeah'
        return 'soy un colaborador'

class VersionManager(object):

    def __init__(self, colaborador=None):
        self.colaborador = colaborador

 #   def check_version(self):
 #       return 'lala'


    def check(self, repo, requirements):
        if self.colaborador:
            self.colaborador.algo_que_debe_llamarse()
        return '{} has no outdated packages'.format(repo)
