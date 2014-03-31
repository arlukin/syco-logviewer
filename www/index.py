#!/usr/bin/env python

import os
from datetime import date, timedelta
import cgitb;

from mysql import get_signed
format(os.environ["REMOTE_USER"])

signed_list = get_signed()
datum_dicu = {}
datum_dicu_date = {}
row = signed_list.fetchall()
for value in row:
    datum_dicu.update({value[0]: value[1]})
    datum_dicu_date.update({value[0]: value[2]})

num = 0
for num in range(1, 20):
    whatdate = str(date.today() - timedelta(num))
    if whatdate in datum_dicu:
        user = datum_dicu[whatdate]
    else:
        user = "Unsigned"

    if whatdate in datum_dicu_date:
        signdate = datum_dicu_date[whatdate]
    else:
        signdate = ""

    print """<tr><td><h5><a href="logs.py?view_date={0}">{0}</a></h5></td><td><h5>{1}</h5></td><td><h5>{2}</h5></td></tr>""".format(
        date.today() - timedelta(num), user, signdate)
    num = num + 1

