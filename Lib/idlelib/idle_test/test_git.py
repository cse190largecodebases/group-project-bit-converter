import unittest
from tkinter import Tk
from idlelib.git import SourceControlGUI
import tempfile

class TestSourceControlGUI(unittest.TestCase):

    def test_perform_repo(self):
        app = SourceControlGUI()
        
        # Test case 1: Existing folder selected, repository not initialized yet
        with tempfile.TemporaryDirectory() as tmpdirname:
            app.perform_repo(tmpdirname)
            check = "New repository initialized:"
            self.assertIn(check, app.status_text.get("1.0",'end-1c'))
                
            # Test case 2: Existing repository selected
            app.perform_repo(tmpdirname)
            check = "Existing repository selected:"
            self.assertIn(check, app.status_text.get("1.0",'end-1c'))

            # Test case 3: File selected instead of directory
            with open(tmpdirname + "/file.py", 'w') as fp:
                fp.write('temporary file contents')
                app.perform_repo(tmpdirname + "/file.py")
                check = "Invalid selection:"
                self.assertIn(check, app.status_text.get("1.0",'end-1c'))


    def test_git_status(self):
        app = SourceControlGUI()
        
        with tempfile.TemporaryDirectory() as tmpdirname:
            app.perform_repo(tmpdirname)
            repo_status = app.repo.git.status()
            self.assertIsNotNone(repo_status)


    def test_git_remove(self):
        app = SourceControlGUI()
        
        # Test Case 1: Remove a file that does not exist
        with tempfile.TemporaryDirectory() as tmpdirname:
            app.perform_repo(tmpdirname)
            app.perform_remove("non_existant_file.py")
            expected_output = "File not found" 
            self.assertIn(expected_output, app.status_text.get("1.0",'end-1c')) 

            # Test Case 2: Remove a file that exists
            with open(tmpdirname + "/file.py", 'w') as fp:
                fp.write('temporary file contents')
                app.perform_add("file.py")
                app.perform_remove("file.py")
                expected_output = "Removed:"
                self.assertIn(expected_output, app.status_text.get("1.0", 'end-1c'))


    def test_git_add(self):
        app = SourceControlGUI()

        # Test Case 1: File not Found
        with tempfile.TemporaryDirectory() as tmpdirname:
            app.perform_repo(tmpdirname)
            app.perform_add("non_existing_file.txt")
            expected_output = "File not found:"
            self.assertIn(expected_output, app.status_text.get("1.0",'end-1c'))
            
            #Test Case 2: Successfully add file
            with open(tmpdirname + "/file.py", 'w') as fp:
                fp.write('temporary file contents')
                app.perform_add("file.py")
                expected_output = "Added:"
                self.assertIn(expected_output, app.status_text.get("1.0",'end-1c'))


if __name__ == '__main__':
    unittest.main()
