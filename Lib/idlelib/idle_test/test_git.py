import unittest
from tkinter import Tk
from idlelib.git import SourceControlGUI

class TestSourceControlGUI(unittest.TestCase):

    def test_perform_repo(self):
        app = SourceControlGUI()
        
        # Test case 1: Existing repository selected
        app.perform_repo("/Users/ken/Desktop/group-project-bit-converter")
        check = "Existing repository selected:"
        self.assertIn(check, app.status_text.get("1.0",'end-1c'))

        # Test case 2: Non-existing repository selected
        # Will need to change this path everytime this test runs as it will not be newly initialized anymore.
        app.perform_repo("/Users/ken/Desktop/test_init5")
        check = "New repository initialized:"
        self.assertIn(check, app.status_text.get("1.0",'end-1c'))

        # Test case 3: Invalid file selection
        app.perform_repo("/Users/ken/Desktop/3e.jpeg")
        check = "Invalid selection:"
        self.assertIn(check, app.status_text.get("1.0",'end-1c'))


    def test_git_status(self):
        app = SourceControlGUI()

        # Will need to change to a working repo that has git initialized
        app.perform_repo("/Users/ken/Desktop/group-project-bit-converter")

        repo_status = app.repo.git.status()
        expected_phrase = "Your branch is up to date with"
        self.assertIn(expected_phrase, repo_status)


if __name__ == '__main__':
    unittest.main()
