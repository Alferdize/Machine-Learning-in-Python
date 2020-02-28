import os


files = [arff for arff in os.listdir(".") if arff.endswith(".arff")]


# def toCsv(content):
#     data = False
#     header = ""
#     newContent = []
#     for line in content:
#         if not data:
#             if "@ATTRIBUTE" in line:
#                 attri = line.split()
#                 columnName = attri[attri.index("@ATTRIBUTE")+1]
#                 header = header + columnName + ","

#             elif "@DATA" in line:
#                 data = True
#                 header = header[:-1]
#                 header += '\n'
#                 newContent.append(header)
#         else:
#             newContent.append(line)            
#     return newContent




# for file in files:
#     with open(file,"r") as inFile:
#         content = inFile.readlines()
#         name,ext = os.path.splitext(inFile.name)
#         new = toCsv(content)
#         with open(name+".csv","w") as outFile:
#             outFile.writelines(new)




"""trans multi-label *.arff file to *.csv file."""
import re


def trans_arff2csv(file_in, file_out):
    """trans *.arff file to *.csv file."""
    columns = []
    data = []
    with open(file_in, 'r') as f:
        data_flag = 0
        for line in f:
            if line[:2] == '@a':
                # find indices
                indices = [i for i, x in enumerate(line) if x == ' ']
                columns.append(re.sub(r'^[\'\"]|[\'\"]$|\\+', '', line[indices[0] + 1:indices[-1]]))
            elif line[:2] == '@d':
                data_flag = 1
            elif data_flag == 1:
                data.append(line)

    content = ','.join(columns) + '\n' + ''.join(data)

    # save to file
    with open(file_out, 'w') as f:
        f.write(content)


if __name__ == '__main__':
    from multi_label.arff2csv import trans_arff2csv

    # setting arff file path
    for file in files:
    # trans
        trans_arff2csv(file_attr_in, "Hash"+".csv")