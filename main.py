#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.

try:
    import unicornhathd # 16x16
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicornhathd


# ./lib/unicorn-hat-hd/examples/*.py

try:
    unicornhathd.rotation(0)
    unicornhathd.brightness(1.0)

except KeyboardInterrupt:
    unicornhathd.off()
