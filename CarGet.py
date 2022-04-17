import csv
import os
from os.path import exists


def sampler(saveManySamples: bool):
    sample = 0
    file = open(r'C:\Users\simon\PycharmProjects\SpectrumAnalysor\Samples\TraceFile.CSV')
    csvreader = csv.reader(file)
    total = []
    header = next(csvreader)
    total.append(header)
    rows = []
    for row in csvreader:
        rows.append(row)
        total.append(row)
    while True:
        fileName = r'C:\Users\simon\PycharmProjects\SpectrumAnalysor\Samples\Results\sample' + str(sample) + '.csv'
        if not os.path.exists(fileName):
            break
        if saveManySamples:
            sample = sample + 1
    with open(r'C:\Users\simon\PycharmProjects\SpectrumAnalysor\Samples\Results\sample' + str(sample) + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(total)
    return fileName
