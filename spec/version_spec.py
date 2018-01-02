# -*- coding: utf-8 -*-
from doublex import Spy
from expects import expect, equal
from doublex_expects import have_been_called

from version_manager import VersionManager, Colaborador

A_REPO = "Repo Name"
AN_EMPTY_REQUIREMENTS_FILE = {}
A_REQUIREMENTS_FILE_WITH_SOME = "jquery"

with describe('Check if all given libraries are updated'):

    with context('Given an empty library list'):
        with it('return name of the program and outdated library list as nothing'):

            version_manager = VersionManager()
            result = version_manager.check(A_REPO,AN_EMPTY_REQUIREMENTS_FILE)

            expect(result).to(equal("Repo Name has no outdated packages"))

    with context('Given a library list with some element'):
        with before.each:
            self.colaborador = Spy()
            self.version_manager = VersionManager(self.colaborador)

        with it('check if the method that check the list is called'):

            self.version_manager.check(A_REPO, A_REQUIREMENTS_FILE_WITH_SOME)

            expect(self.colaborador.algo_que_debe_llamarse).to(have_been_called)
