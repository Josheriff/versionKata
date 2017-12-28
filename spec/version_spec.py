# -*- coding: utf-8 -*-
# from doublex import Spy
from expects import expect
# from doublex_expects import have_been_called_with

A_REPO = "Repo Name"
AN_EMPTY_REQUIREMENTS_FILE = {}

with describe('Check if all given libraries are updated'):

    with context('Given an empty library list'):
        with it('return name of the program and outdated library list as nothing'):
            expect(my_sut.check(A_REPO,AN_EMPTY_REQUIREMENTS_FILE).equal("Repo Name has no outdated packages"))
