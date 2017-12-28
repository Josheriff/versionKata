# -*- coding: utf-8 -*-
# from doublex import Spy
from expects import expect, equal
import version_manager
# from doublex_expects import have_been_called_with

A_REPO = "Repo Name"
AN_EMPTY_REQUIREMENTS_FILE = {}

with describe('Check if all given libraries are updated'):

    with context('Given an empty library list'):
        with it('return name of the program and outdated library list as nothing'):

            result = version_manager.check(A_REPO,AN_EMPTY_REQUIREMENTS_FILE)

            expect(result).to(equal("Repo Name has no outdated packages"))
