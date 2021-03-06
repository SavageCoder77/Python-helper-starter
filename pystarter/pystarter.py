def pystarterVersion():
    return "1.5.1"


def pystarterCommands():
    return """
Command list:

pystarter create <option>

option can be left blank

Options you can use (do not use <> in command arguments):
    <git> for git only projects
    <python> for python only projects
    <all> for both git and python projects (setup.py not included)
    <setup> to include a setup.py template
    or leave it blank for for projects with git and python

pystarter clean

Clean out pyc files and __pycache__ files
           """
