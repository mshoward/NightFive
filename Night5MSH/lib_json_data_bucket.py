"""
Name:
    json_data_bucket

v0.1.1-alpha.1

Description:
    Data wrapper -- like a tuple. But with more strings.

Class Overview:
    Constructor:
        json_data_bucket(self,
                         string: p_key=None,
                         stringable_object: p_value=None)
    Class Members:
        Instance Members:
            string: key
            stringable_object: value
            boolean: set_key(obj_ref: self, string: p_key=None)
            boolean: set_value(obj_ref: self, p_value=None)
            string: get()
        Non-Instance Class Members:

        Static Members:

todo: implement implicitly stringable qualities to this thing.

"""
