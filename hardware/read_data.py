#!/usr/bin/env python
#  -*- coding: utf-8 -*-

from __future__ import print_function
from time import sleep
from sys import stdout
from daqhats import mcc118, OptionFlags, HatIDs, HatError
from daqhats_utils import select_hat_device, enum_mask_to_string, \
    chan_list_to_mask
import pandas as pd

CURSOR_BACK_2 = '\x1b[2D'
ERASE_TO_END_OF_LINE = '\x1b[0K'


def get_data(scan_rate: float, samples_per_channel: int, channels: list, channel_names: list):
    channel_mask = chan_list_to_mask(channels)
    num_channels = len(channels)
    options = OptionFlags.DEFAULT
    try:
        # Select an MCC 118 HAT device to use.
        address = select_hat_device(HatIDs.MCC_118)
        hat = mcc118(address)

        actual_scan_rate = hat.a_in_scan_actual_rate(num_channels, scan_rate)

        # Configure and start the scan.
        hat.a_in_scan_start(channel_mask, samples_per_channel, scan_rate,
                            options)

        data = {}
        try:
            raw_data = read_and_display_data(
                hat, samples_per_channel, num_channels)
            for name, i in zip(channel_names, range(num_channels)):
                data[name]=raw_data[i]
            data = pd.DataFrame(data)
            data["Time"] = [i/(1/scan_rate) for i in range(len(data.index))]
            data.set_index("Time", inplace=True)
        except KeyboardInterrupt:
            # Clear the '^C' from the display.
            print(CURSOR_BACK_2, ERASE_TO_END_OF_LINE, '\n')
            hat.a_in_scan_stop()
        hat.a_in_scan_cleanup()
        return data

    except (HatError, ValueError) as err:
        print('\n', err)


def read_and_display_data(hat, samples_per_channel, num_channels):
    total_samples_read = 0
    read_request_size = 500
    timeout = 5.0

    data = []
    while total_samples_read < samples_per_channel:
        read_result = hat.a_in_scan_read(read_request_size, timeout)
        data.append(read_result.data)
        # Check for an overrun error
        if read_result.hardware_overrun:
            print('\n\nHardware overrun\n')
            break
        elif read_result.buffer_overrun:
            print('\n\nBuffer overrun\n')
            break

        samples_read_per_channel = int(len(read_result.data) / num_channels)
        total_samples_read += samples_read_per_channel

    data = [item for sublist in data for item in sublist]
    data = transform_data(data, num_channels)
    return data
    print('\n')


def transform_data(data: list, number_of_channels: int):
    new_data = [[] for _ in range(number_of_channels)]
    for i, value in enumerate(data):
        sensor_index = i % number_of_channels
        new_data[sensor_index].append(value)
    return new_data


if __name__ == '__main__':
    data = get_data(10000, 10000, [1, 2], ["mic", "ir"])
    print(data)
