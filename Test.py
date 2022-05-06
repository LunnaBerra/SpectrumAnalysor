import CSVtransfer

# 1: Creates CSV and a copy
import CarGet
from time import sleep
import pandas as pd
from scipy import stats
import OutlierAnalyser


def testing(saveManySamples: bool, endTime: int, freqCenter: float, freqSpan: float, stopOnDeviation: bool, abort: bool,
            ampHigh: float, ampLow: float):
    timeCompleted = 0
    time = 0
    times = 0
    while timeCompleted < endTime:
        if abort:
            break
        new_time = CSVtransfer.runner(freqCenter, freqSpan)
        time = time + new_time
        times = times + 1
        fileName = r'C:\Users\simon\PycharmProjects\SpectrumAnalysor\Samples\TraceFile.csv'
        freqStart = freqCenter - (freqSpan / 2) + 1
        freqEnd = freqCenter + (freqSpan / 2) - 1
        outlier = OutlierAnalyser.init(fileName, freqStart, freqEnd, ampHigh, ampLow)
        if outlier:
            CarGet.sampler(saveManySamples)
            if stopOnDeviation:
                print(time/times)
                break
        timeCompleted = timeCompleted + 10.5
    print(time / times)



# 2: Checks for outlier

# 3.1: If not stop on deviation and save CSV, save CSV and continue
# 3.2: If stop on deviation, save CSV on stop test
# 3.3: If not stop on deviation and not save CSV, only save latest outlier

# 4 Stop after test time is over
