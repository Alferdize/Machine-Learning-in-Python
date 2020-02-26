import os


files = [arff for arff in os.listdir(".") if arff.endswith(".arff")]


def toCsv(content):
    data = False
    header = ""
    newContent = []
    for line in content:
        if not data:
            if "@ATTRIBUTE" in line:
                attri = line.split()
                columnName = attri[attri.index("@ATTRIBUTE")+1]
                header = header + columnName + ","

            elif "@DATA" in line:
                data = True
                header = header[:-1]
                header += '\n'
                newContent.append(header)
        else:
            newContent.append(line)            
    return newContent




for file in files:
    with open(file,"r") as inFile:
        content = inFile.readlines()
        name,ext = os.path.splitext(inFile.name)
        new = toCsv(content)
        with open(name+".csv","w") as outFile:
            outFile.writelines(new)