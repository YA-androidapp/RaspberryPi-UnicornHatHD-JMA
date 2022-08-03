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


def get_pref(area_id):
    response = requests.get(JMA_JSON_BASEURL + area_id + '.json')

    if response.status_code != 200:
        return {}

    data = json.loads(response.text, object_pairs_hook=OrderedDict)

    times = []
    area_name_wc = []
    weather_icons = []
    weather_telops = []

    area_publishing_office = ''
    for area in data:
        for ts in area['timeSeries']:
            if len(ts['timeDefines']) == 7:
                times = [format_date(n) for n in ts['timeDefines']]
                area = ts['areas'][0]
                if 'weatherCodes' in area:
                    area_name_wc = area['area']['name']
                    weather_telops = [JMA_TELOPS[n] for n in area['weatherCodes']]
                    weather_colors = [JMA_COLORS[n] for n in area['weatherCodes']]

    return {
        "id": area_id,
        "times": times,
        "pref": area_name_wc,
        "telops": weather_telops,
        "colors": weather_colors
    }


if __name__ == '__main__':
    unicornhathd.rotation(0)
    unicornhathd.brightness(0.6)

    try:
        for i, area_id in enumerate(JMA_AREA.keys()):
            print(
                get_pref(area_id)
            )

        time.sleep(300)

        unicornhathd.off()
    except KeyboardInterrupt:
        unicornhathd.off()