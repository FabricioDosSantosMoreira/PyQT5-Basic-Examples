Using pyuic5 to Convert .ui Files to Python Code:

    pyuic5 is a command-line utility that comes with PyQt5, a set of Python bindings for Qt libraries. 
    It is used to convert .ui files created with Qt Designer into Python code. 
    This allows you to create the GUI with Qt Designer and then use the generated Python code in your PyQt5 applications.


Steps to Use pyuic5: 

    1. Create a .ui File with Qt Designer
        - Open Qt Designer and create your GUI. Save the file with a .ui extension, for example, mydesign.ui.

    2. Convert the .ui File to Python Code
        - Open your CLI(command-line interface)
        - pyuic5 -x "path_to_your_.ui" -o "desired_path_to_your_.py"

    3. Additional Options
        -h, --help: Show help message and exit.
        -o <file>: Specify the output file name.
        -x: Generate additional code to test and display the widget (adds a main() function).


Additional Info About pyuic5:

    1. Location of pyuic5
        - Windows: C:\Users\<your_username>\AppData\Local\Programs\Python\Python<version>\Scripts\pyuic5.exe

    2. Running pyuic
        - Windows: To run any pyuic command you must first add to your PATH variable


Example:

    1. Windows
        pyuic5 -x "C:\Users\<your_username>\OneDrive\Workspace\pyqt5_examples\example.ui" -o "C:\Users\<your_username>\OneDrive\Workspace\pyqt5_examples\example.py"
