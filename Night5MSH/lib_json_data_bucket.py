"""
Description: Data wrapper -- like a tuple. But with more strings.

v0.1.1-alpha.3

Class Overview:
    Constructor:
        json_data_bucket(self,
                         string: p_key=None,
                         stringable: p_value=None)
    Class Members:
        Instance Members:
            string: key
            stringable_object: value
            boolean: set_key(obj_ref: self, string: p_key=None)
            boolean: set_value(obj_ref: self, p_value=None)
            boolean: set(obj_ref: self,
                         string: p_key=None,
                         stringable: p_value=None)
            string: get()
        Non-Instance Class Members:

        Static Members:

TODO: implement implicitly stringable qualities to this thing.

"""
from json_exception import json_exception


class json_data_bucket:
    """
    Name: json_data_bucket.  Almost a tuple.  But more friendly.

    v0.1.1-alpha.3

    Description:
        Data wrapper -- like a tuple. But with more strings.

    Class Overview:
        Constructor:
            json_data_bucket(self,
                            string: p_key=None,
                            stringable: p_value=None)
        Class Members:
            Instance Members:
                string: key
                stringable_object: value
                boolean: set_key(obj_ref: self, string: p_key=None)
                boolean: set_value(obj_ref: self, p_value=None)
                boolean: set(obj_ref: self,
                            string: p_key=None,
                            stringable: p_value=None)
                string: get()
            Non-Instance Class Members:

            Static Members:

    TODO: implement implicitly stringable qualities to this thing.
    """

    def __init__(self, p_key=None, p_value=None):
        """
        Construct a fully formed data wrapper.

            Throws json_exception otherwise.
        """
        self.key = str(p_key)
        self.value = p_value
        self.ret = None
        if (p_key is None) or (p_value is None):
            self.ret = json_exception(
                p_msg="creation of a data container malformed.")
            # todo: something something handle the failure
            self.ret.raise_me(True)

    def set_key(self, p_key=None):
        """Check if p_key is not None, then set it."""
        # todo: look into p_key.__get_attr__(**kwargs) etc
        if not (p_key is None):
            self.key = str(p_key)
            return True
        return False
    def set_value(self, p_value=None):

