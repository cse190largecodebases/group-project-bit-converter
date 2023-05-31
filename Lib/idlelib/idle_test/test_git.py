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

    def test_git_remove(self):
        app = SourceControlGUI()

        # Test Case 1: Remove a file that does not exist
        app.perform_repo("/Users/ericvu/CSE190/test")
        app.perform_remove("/Users/ericvu/CSE190/test/non_existing_file.txt")
        expected_output = "File not found:" 
        self.assertIn(expected_output, app.status_text.get("1.0",'end-1c')) 

        # Test Case 2: Remove a file that exists
        app.perform_repo("/Users/ericvu/CSE190/test")
        app.perform_add("Users/ericvu/CSE190/test/existingfile.txt")
        app.perform_remove("Users/ericvu/CSE190/test/existingfile.txt")
        expected_output = "Removed:"
        self.assertIn(expected_output, app.status_text.get("1.0", 'end-1c'))


if __name__ == '__main__':
    unittest.main()
