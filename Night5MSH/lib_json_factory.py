#!/usr/bin

"""Constructs a JSON string from the things handed to it."""

"""
Description:
    An object that creates and holds a json data structure. Performance is not
        taken into consideration.

Note, in general, type_expected_or_returned: symbol_name.

Constructor:
    json_factory(self, json_factory: parent=None)
Class Members:
    Instance Members:
        json_data_bucket:   content[]
        boolean:            add_item(json_data_bucket item)
        boolean:            remove_item(string: key)
        json_data_bucket:   lookup(string: key)
        string[]:           keys()



"""
