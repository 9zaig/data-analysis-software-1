# we need to filter all the xml to only those who contain LMZC in their name

from pathlib import Path
import os

class Filter:

    def __init__(self, path:str):
        """
        initlization for filtering all the files

        Args:
            path (str): path of the file we want to check if it is an xml file and had LMZC in the name
        """

        self.file = path
        self.SUBSTRING = "LMZ"

    
    # def is_xml(self):
    #     """
    #     check if the input file is an xml file
    #
    #     Returns:
    #         boleen: return True if the file is an xml file
    #     """
    #     # Is it necessary to checking xml file or not?
    #     if self.file.endswith(".xml"):
    #         return True
    #     else:
    #         return False

    def has_LMZC(self):
        """
        check if the file name contain the substring

        Returns:
            boleen: return True if the substring is found inside the filename
        """

        self.file_name = Path(self.file).stem

        if self.SUBSTRING in self.file_name:
            return True
        else:
            return False



