
import pydicom
import numpy as np
import os

"""Go through all items in the dataset and print them with custom format


    """


def myprint(ds, indent=0):
    indent_string = "   " * indent
    next_indent_string = "   " * (indent + 1)

    for data_element in ds:

        repr_value = repr(data_element.value)
        if len(repr_value) > 50:
            repr_value = repr_value[:50] + "..."
        print("{0:s} {1:s} = {2:s}".format(indent_string,
                                           data_element.name,
                                           repr_value))


ospath = r"6183028_astm_cc_class_20_SERVICE2v1.dcs"
ds = pydicom.read_file(ospath)
myprint(ds)





