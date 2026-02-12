import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Create a mock module for tkinter BEFORE importing main
mock_tkinter = MagicMock()

# Mock the Tk class and its mainloop method
class MockTk:
    def __init__(self, *args, **kwargs):
        pass
    def mainloop(self):
        pass
    def title(self, *args): pass
    def geometry(self, *args): pass
    def config(self, *args, **kwargs): pass

# Mock the StringVar class
class MockStringVar:
    def __init__(self, *args, **kwargs):
        self.value = ""
    def get(self):
        return self.value
    def set(self, value):
        self.value = value

mock_tkinter.Tk = MockTk
mock_tkinter.StringVar = MockStringVar
# Mock other widgets
mock_tkinter.Label = MagicMock()
mock_tkinter.Button = MagicMock() # This is the class, so calling it returns a mock instance
mock_tkinter.Entry = MagicMock()
mock_tkinter.Frame = MagicMock()
mock_tkinter.Text = MagicMock()
mock_tkinter.Scrollbar = MagicMock()

# Mock constants
mock_tkinter.VERTICAL = 'vertical'
mock_tkinter.RIDGE = 'ridge'
mock_tkinter.RIGHT = 'right'
mock_tkinter.Y = 'y'
mock_tkinter.BOTH = 'both'
mock_tkinter.END = 'end'

# Assign the mock module to sys.modules
sys.modules['tkinter'] = mock_tkinter
sys.modules['tkinter.messagebox'] = MagicMock()
sys.modules['pymysql'] = MagicMock()

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now import main. It will execute root = Tk(), obj = EmployeeSystem(root), root.mainloop()
# But since we mocked Tk and mainloop, it should finish immediately.
import main

class TestClearButton(unittest.TestCase):
    def test_clear_button_command(self):
        # Create a fresh instance for testing
        root = MockTk()
        # We need to instantiate it to test
        # app = main.EmployeeSystem(root) # We will do this inside the patch context below

        # We need to find the "Clear" button.
        # Since we can't easily introspect the widgets created in __init__ (they are local variables mostly),
        # we have to rely on mocking Button during the init.

        # Let's re-instantiate EmployeeSystem but with Button patched so we can capture the calls
        with patch('main.Button') as MockButton:
            app = main.EmployeeSystem(root)

            # Find the call for the "Clear" button
            clear_button_call = None
            for call in MockButton.call_args_list:
                # call.kwargs contains the arguments
                kwargs = call.kwargs
                if kwargs.get('text') == "Clear":
                    clear_button_call = call
                    break

            self.assertIsNotNone(clear_button_call, "Could not find a button with text='Clear'")

            # Check if command is bound
            command = clear_button_call.kwargs.get('command')

            # This assertion confirms the current bug (missing command)
            # Or if we want the test to pass only when fixed, we assert IsNotNone
            if command is None:
                print("\n[TEST INFO] Clear button currently has NO command (Expected failure).")
                # Fail the test to confirm the bug
                self.fail("Clear button has no command assigned!")
            else:
                print("\n[TEST INFO] Clear button HAS a command.")
                # If command exists, we could check if it is the clear method
                # But since 'clear' method doesn't exist on the class yet, we can't check equality easily

            # Verify the clear logic
            # Set some values first
            app.var_emp_code.set("123")
            app.var_name.set("Test Name")

            # Call the command (which should be self.clear)
            command()

            # Verify values are reset
            self.assertEqual(app.var_emp_code.get(), "", "Emp code should be cleared")
            self.assertEqual(app.var_name.get(), "", "Name should be cleared")

            # Verify text widgets are cleared
            # The mock Text widget should have received delete('1.0', END)
            # app.txt_address is a MagicMock
            app.txt_address.delete.assert_called_with('1.0', 'end')

if __name__ == '__main__':
    unittest.main()
