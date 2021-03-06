# -*- coding: utf-8 -*-
from doublex import Spy
from expects import expect, equal
from doublex_expects import have_been_called

from version_manager import VersionManager

A_REPO = "Repo Name"
AN_EMPTY_REQUIREMENTS_LINE = None
A_REQUIREMENTS_FILE_WITH_SOME = "jquery"

with describe('Check if all given libraries are updated'):

    with context('Given an empty library list'):
        with it('return name of the program and outdated library list as nothing'):

            version_manager = VersionManager()
            result = version_manager.check_file(AN_EMPTY_REQUIREMENTS_LINE)

            expect(result).to(equal('this project has no package list'))

    with context('Given a library list with some element'):
        with before.each:
            self.check_repo = Spy()
            self.version_manager = VersionManager(self.check_repo)

        with it('check if the method that check the list is called'):

            self.version_manager.check_file(A_REQUIREMENTS_FILE_WITH_SOME)

            expect(self.check_repo.check_repository).to(have_been_called)
