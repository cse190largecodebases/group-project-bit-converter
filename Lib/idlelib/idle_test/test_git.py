import unittest
from tkinter import Tk
from idlelib.git import SourceControlGUI

class TestSourceControlGUI(unittest.TestCase):
    def test_git_status(self):
        app = SourceControlGUI()

        # Will need to change to a working repo that has git initialized
        app.perform_repo("/Users/ken/Desktop/group-project-bit-converter")

        repo_status = app.repo.git.status()
        expected_phrase = "Your branch is up to date with"
        self.assertIn(expected_phrase, repo_status)

        # Cleanup


if __name__ == '__main__':
    unittest.main()
