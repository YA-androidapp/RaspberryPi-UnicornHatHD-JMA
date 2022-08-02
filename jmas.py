#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.

try:
    import unicornhathd # 16x16
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicornhathd


#


from collections import OrderedDict
from datetime import datetime
import json
import os
import requests
import sys
import time

from const import JMA_AREA, JMA_ICON_BASEURL, JMA_COLORS, JMA_JSON_BASEURL, JMA_TELOPS


def format_date(dt):
    return datetime.strftime(
        datetime.strptime(
            dt,
            '%Y-%m-%dT%H:%M:%S%z'
        ),
        '%m/%d'
    )


def set_xy_color(x, y, r, g, b):
    u_width, u_height = unicornhathd.get_shape()
    unicornhathd.set_pixel(u_width - 1 - x, y, r, g, b)
    unicornhathd.show()


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

                area = ts['areas'][0]
                if 'weatherCodes' in area:
                    area_name_wc = area['area']['name']
                    print('area_name_wc', area_name_wc, i)

                    weather_telops = [JMA_TELOPS[n] for n in area['weatherCodes']]
                    print('weather_telops', ' '.join(weather_telops))

                    weather_colors = [JMA_COLORS[n] for n in area['weatherCodes']]
                    for j, col in enumerate(weather_colors):
                        print((j, i), col)
                        set_xy_color(j, i, *col)


if __name__ == '__main__':
    unicornhathd.rotation(0)
    unicornhathd.brightness(0.6)

    try:
        for i, area_id in enumerate(JMA_AREA.keys()):
            get_pref(area_id, i)

        time.sleep(300)

        unicornhathd.off()
    except KeyboardInterrupt:
        unicornhathd.off()