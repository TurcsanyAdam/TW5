def import_file(file_name):

    with open(file_name, "r") as f:
        lines= f.readlines()

    table = [element.replace("\n", "").split(",") for element in lines]
    return table




def export_file(table, file_name):
    pass
