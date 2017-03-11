"""
Some Doc.   0.1.1-alpha.3

Some other doc.
"""
import sys


class json_exception(Exception):
    """Somedoc str."""

    def __init__(self, p_msg="msg"):
        """
        Initialization for json_exception.

        Calls
        """
        super().__init__()
        self.msg = p_msg
        print(p_msg, sep=' ', end='\n', file=sys.stderr)

    def raise_me(self, p_throwit=False):
        """Some str."""
        # todo
        if bool(p_throwit):
            raise self
        return self.msg
