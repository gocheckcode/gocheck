import argparse
import os

class CLI:
    """
    This class is the entry point to the program
    """

    def __init__(self, file, dir):
        """ Constructor """
        self.file = file
        self.dir = dir
        self.entry()
       
    def entry(self):
        """
        CLI arguments for the program
        """
        if self.file is not None:
            if os.path.isfile(self.file):
                # The file is a real file and can be parsed
                self.search_file(self.file)
        if self.dir is not None:
            if os.path.isdir(self.dir):
                # The directory is real on the filesystem and can be looped through
                self.search_dir()

    def search_file(self, file):
        """
        Call the search function in search.py with the file as the input
        """
        print(file) # eventually will call some function in search.py

    def search_dir(self):
        """
        Loop through the directory, get a list of all the files
        Use that list and send each file to the search_file function
        """
        for subdir, dirs, files in os.walk(self.dir):
            for file in files:
                self.search_file(os.path.join(subdir, file))
        return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='File to check for words')
    parser.add_argument('-d', '--directory', help='Directory to scan for words')

    args = parser.parse_args()

    if not (args.file or args.directory):
        parser.error('No action requested, add -f or -d')

    cli = CLI(args.file, args.directory)

if __name__ == "__main__":
    main()