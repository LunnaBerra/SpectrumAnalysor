import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


def plotting(fileName, mean, frequencies, outlierLimit):
    # Plotting data-points
    df = pd.read_csv(fileName)
    fig = px.line(df, x='Frequency in Hz', y='Power in dBm', title='Power Received by Frequency')

    i = 0
    outlierFrequncies = []
    while i < len(frequencies):
        outlierFrequncies.append(float(frequencies.iloc[i]))
        i = i + 1
    x1 = outlierFrequncies

    # Plotting mean and limits
    y1 = [float(mean)] * len(x1)
    fig.add_trace(go.Scatter(x=x1, y=y1,
                             mode='lines',
                             name='Mean value of sample'))
    y2 = [outlierLimit + float(mean)] * len(x1)
    fig.add_trace(go.Scatter(x=x1, y=y2,
                             mode='lines',
                             name='Upper limit of normal data-points'))
    y3 = [-outlierLimit + float(mean)] * len(x1)
    fig.add_trace(go.Scatter(x=x1, y=y3,
                             mode='lines',
                             name='Lower limit of normal data-points'))
    fig.show()
