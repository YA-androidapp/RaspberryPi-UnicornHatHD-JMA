#!/usr/bin/python3
# -*- coding: utf-8 -*-
from collections import OrderedDict
from datetime import datetime
import json
import os
import requests
import sys
import time

from const import JMA_AREA, JMA_ICON_BASEURL, JMA_COLORS, JMA_JSON_BASEURL, JMA_TELOPS


DEBUG_ON_PC = False # Raspberry Pi上ではFalse、PCでのデバッグ時はTrueに変更


if DEBUG_ON_PC == False:
    from rpi_ws281x import PixelStrip, Color

    LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
    LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
    LED_COUNT = 32        # Number of LED pixels.
    LED_DMA = 10          # DMA channel to use for generating signal (try 10)
    LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
    LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).


# | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 |
# | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 |
# | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
# | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |

# | 24 | 16 | 08 | 00 |
# | 25 | 17 | 09 | 01 |
# | 26 | 18 | 10 | 02 |
# ...
# | 31 | 23 | 15 | 07 |
def set_xy_color(x, y, color):
    if 0 <= x <= 3 and 0 <= y <= 7:
        i = 8 * ( 3 - x ) + y
        if DEBUG_ON_PC == False:
            strip.setPixelColor(i, color)
            strip.show()
        else:
            print(i, x, y)


def format_date(dt):
    return datetime.strftime(
        datetime.strptime(
            dt,
            '%Y-%m-%dT%H:%M:%S%z'
        ),
        '%m/%d'
    )


def main():
    for i, area_id in enumerate(JMA_AREA.keys()):
        get_pref(area_id, i)


def get_pref(area_id, i):
    response = requests.get(JMA_JSON_BASEURL + area_id + '.json')

    if response.status_code != 200:
        sys.exit()

    data = json.loads(response.text, object_pairs_hook=OrderedDict)

    times = []

    area_publishing_office = ''
    for area in data:
        for ts in area['timeSeries']:
            if len(ts['timeDefines']) == 7:
                if i == 0 and len(times) == 0:
                    times = [format_date(n) for n in ts['timeDefines']]
                    print('times', ' '.join(times), '\n')

                area_name_wc = []
                weather_icons = []
                weather_telops = []

                # for area in ts['areas']:
                area = ts['areas'][0]

                if 'weatherCodes' in area:
                    area_name_wc = area['area']['name']
                    print('area_name_wc', area_name_wc, i)

                    weather_telops = [JMA_TELOPS[n] for n in area['weatherCodes']]
                    print('weather_telops', ' '.join(weather_telops))

                    weather_colors = [JMA_COLORS[n] for n in area['weatherCodes']]
                    for j, col in enumerate(weather_colors):
                        if DEBUG_ON_PC == False:
                            set_xy_color(j, i, Color(*col))
                        else:
                            print((j, i), col)

                print('')
                # end for


def clear_color():
    if DEBUG_ON_PC == False:
        for c in range(LED_COUNT):
            strip.setPixelColor(c, Color(0, 0, 0))
        strip.show()


if __name__ == '__main__':
    if DEBUG_ON_PC == False:
        strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        strip.begin()
    try:
        main()
        time.sleep(300)
        clear_color()

    except KeyboardInterrupt:
        clear_color()