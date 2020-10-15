#!/usr/bin/env python3

import re

pattern = r"^([\w .]*), ([\w .]*)$"

def rearrange_name(name):
    result = re.search(pattern, name)

    if result is None:
        return name

    return f"{result[2]} {result[1]}"