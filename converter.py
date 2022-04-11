from tika import parser
import re
import csv
import sys
import os.path

transactionPattern = '(\d{0,2}\.\d{0,2}\.\d{4})\W(\d{0,2}\.\d{0,2}\.\d{4})\W([\w\-Üü]+)\W([\w\sÄäÜüÖöß\-\.\/+*]+)(\-?\d+,\d{2}\W\w+)'

def readPdf(pdfFilePath):
    if(os.path.exists(pdfFilePath)):
        return parser.from_file(pdfFilePath)
    else:
        sys.exit("pdf does not exist")

def writeCSV(csvFilePath, contentList):
    with open(csvFilePath, 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for line in contentList:
         wr.writerow(line)

def extractTransactions(rawText):
    text = str(rawText.get('content')).replace('\n', ' ')
    return re.findall(transactionPattern, text)


if(len(sys.argv) != 3):
        sys.exit("usage converter.py /path/to/pdf /path/for/csv")

pdfFile = sys.argv[1]
csvFile = sys.argv[2]

rawText = readPdf(pdfFile)
transactions = extractTransactions(rawText)
writeCSV(csvFile, transactions)