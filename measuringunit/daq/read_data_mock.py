import numpy as np
from time import sleep


def get_data(scan_rate: float, samples_per_channel: int, channels: list, channel_names: list):
    num_channels = len(channels)
    duration = samples_per_channel / scan_rate

    # Generate synthetic data for each channel
    data = {}
    time_stamps = np.linspace(0, duration, num=samples_per_channel, endpoint=False).tolist()
    for channel, name in zip(channels, channel_names):
        # Generate random data mimicking sensor outputs; modify as necessary
        data[name] = np.random.normal(loc=0.0, scale=1.0, size=samples_per_channel).tolist()

    data["time"] = time_stamps
    sleep(samples_per_channel/scan_rate)
    return data
