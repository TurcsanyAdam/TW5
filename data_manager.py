def import_file(file_name):

    with open(file_name, "r" as f):
        lines= f.readlines()
        for element in lines:
            element.replace("\n", "")
            element.split(",")
    pass



def export_file(table, file_name):
    pass
