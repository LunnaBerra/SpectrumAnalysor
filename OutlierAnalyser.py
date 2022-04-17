import pandas as pd
from scipy import stats
import plotter


def init(fileName, freqLow: float, freqHigh: float):
    df = pd.read_csv(fileName)
    W_DBm = df.loc[:, lambda df: ['Power in dBm']]

    i = 0
    listOfPoints = []
    while i < len(df.__array__()):
        listOfPoints.append(float(W_DBm.iloc[i]))
        i = i + 1

    meanPoints = stats.trim_mean(W_DBm, 0.25)

    diffs = []
    i = 0
    while i < len(df.__array__()):
        diffs.append(float(abs(meanPoints - float(W_DBm.iloc[i]))))
        i = i + 1

    meanDiffs = stats.trim_mean(diffs, 0.25)

    outlierLimit = 5 * meanDiffs

    outliers = []
    i = 0
    while i < len(df.__array__()):
        if abs(diffs[i]) > outlierLimit:
            outliers.append(i)
        i = i + 1

    frequncies = df.loc[:, lambda df: ['Frequency in Hz']]
    i = 0
    outlierFrequncies = []
    while i < len(outliers):
        outlierFrequncies.append(float(frequncies.iloc[outliers[i]]))
        i = i + 1

    i = 0
    while i < len(outlierFrequncies):
        if outlierFrequncies[i] > freqLow or outlierFrequncies[i] < freqHigh:
            return True

    return False
