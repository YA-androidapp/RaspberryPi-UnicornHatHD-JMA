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
import itertools
import json
import os
import requests
import sys
import time

from const import JMA_AREA, JMA_ICON_BASEURL, JMA_COLORS, JMA_JSON_BASEURL, JMA_TELOPS
from kanto import MAP_POINTS, SEA_POINT


def format_date(dt):
    return datetime.strftime(
        datetime.strptime(
            dt,
            '%Y-%m-%dT%H:%M:%S%z'
        ),
        '%m/%d'
    )


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
        "times": times,
        "area_id": area_id,
        "pref": area_name_wc,
        "telops": weather_telops,
        "colors": weather_colors
    }


if __name__ == '__main__':
    unicornhathd.rotation(90)
    unicornhathd.brightness(0.6)
    u_width, u_height = unicornhathd.get_shape()

    for x, y in itertools.product(range(u_width), range(u_height)):
        unicornhathd.set_pixel(x, y, 0, 100, 0)

    for (x, y) in SEA_POINT:
        unicornhathd.set_pixel(x, y, 0, 0, 102)

    try:
        results = []
        for area_id in JMA_AREA.keys():
            results.append(
                get_pref(area_id)
            )

        for j in range(7):
            for jj in range(j+1):
                unicornhathd.set_pixel(jj, 15, 255, 127, 127)
            unicornhathd.show()

            for i, area_id in enumerate(JMA_AREA.keys()):
                col = [ item for item in results if item['area_id'] == area_id ][0]['colors'][j]
                for (x, y) in MAP_POINTS.get(area_id):
                    unicornhathd.set_pixel(x, y, *col)
            unicornhathd.show()
            time.sleep(3)

            for jj in range(j+1):
                unicornhathd.set_pixel(jj, 15, 0, 0, 0)
            unicornhathd.show()

        unicornhathd.off()
    except KeyboardInterrupt:
        unicornhathd.off()
