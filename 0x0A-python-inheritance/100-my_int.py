
  #!/usr/bin/python3
"""Inherits from list and provides a"""


class MyInt(int):
    """
        Inherits from list and provides a
        method to print sorted list.
    """

    def __eq__(self, other):
        """Inherits from list and provides a"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inherits from list and provides a"""
        return super().__eq__(other)
  