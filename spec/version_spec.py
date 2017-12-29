# -*- coding: utf-8 -*-
from doublex import Spy
from expects import expect, equal
import version_manager
# from doublex_expects import have_been_called_with

A_REPO = "Repo Name"
AN_EMPTY_REQUIREMENTS_FILE = {}
A_REQUIREMENTS_FILE_WITH_SOME = "jquery"

with describe('Check if all given libraries are updated'):

    with context('Given an empty library list'):
        with it('return name of the program and outdated library list as nothing'):

            result = version_manager.check(A_REPO,AN_EMPTY_REQUIREMENTS_FILE)

            expect(result).to(equal("Repo Name has no outdated packages"))

    with context('Given a library list with some element'):
        with it('check if the method that check the list is called'):

            self.check_version = Spy()

            version_manager.check(A_REPO,A_REQUIREMENTS_FILE_WITH_SOME)

            expect(self.check_version).to(have_been_called_with('the library : '.format('here we have a variable conteining the libraries readed')).once)
