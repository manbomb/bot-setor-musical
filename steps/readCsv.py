import csv

def readCsv(path: str) -> list:
    lines = []
    with open(path, encoding='utf-8') as csvFile:
        csvReader = csv.reader(csvFile, delimiter='\t')
        for line in csvReader:
            lines.append(line)
    
    usersLines = lines[1:]
    
    users = list(map(lambda ul: { "nome": ul[0], "email": ul[1], "grupo": ul[2], "comum": ul[3] }, usersLines))

    return users
