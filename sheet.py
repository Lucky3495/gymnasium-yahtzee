from utils import Category

class Sheet:
    """
    A class that represents a Yahtzee sheet.
    """
    def __init__(self) -> None:
        """
        Initilizes a Sheet, will start empty.
        """
        self._round: int = 0
        self._sheet: list[int] = [-1]*13 # -1 means the category is empty, 0 means it is filled with 0
    
    
    def get_empty_categories(self) -> list[Category]:
        """
        Returns a list with all empty categories.
        """
        empty = []
        for value in Category:
            if self._sheet[value] == -1:
                empty.append(value)
        
        return empty
    
    def __getitem__(self, i):
        assert i >= 0 and i <= 12
        return self._sheet[i]
    
    def __setitem__(self, i, value: int):
        assert i >= 0 and i <= 12
        self._sheet[i] = value
