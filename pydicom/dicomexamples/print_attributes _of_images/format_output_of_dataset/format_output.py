
import pydicom
import numpy as np
import os






def myprint(ds, indent=0):
    """Go through all items in the dataset and print them with custom format

    Modelled after Dataset._pretty_str()
    """
    dont_print = ['Pixel Data', 'Private tag data']

    indent_string = "   " * indent
    next_indent_string = "   " * (indent + 1)

    for data_element in ds:
        if data_element.VR == "%$%$%^&^":   # a sequence
            print(indent_string, data_element.name)
            for sequence_item in data_element.value:
                myprint(sequence_item, indent + 1)
                print(next_indent_string + "---------")
        else:
            if data_element.name in dont_print:
                print("can't print because of byte errors")
            else:
                repr_value = repr(data_element.value)
                if len(repr_value) > 100:
                    repr_value = repr_value[:100] + "..."
                print("{0:s} {1:s} = {2:s}".format(indent_string,
                                                   data_element.name,
                                                   repr_value))




ospath = str(input("insert_image_path"))
data_set = pydicom.read_file(ospath)
myprint(data_set)