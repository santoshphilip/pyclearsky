# Copyright (c) 2013 Santosh Philip
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================

import csv
txt = open('b.csv', 'r').read()
lines = txt.splitlines()
rows = [line.split(',') for line in lines]
rows = [[float(cell) for cell in row] for row in rows]
brows = [[row[4], row[6]] for row in rows if row[-1] == 0 and row[-2] == 0]
csv_writer = csv.writer(open('brows.csv', 'w')).writerows(brows)

drows = [[row[5], row[7]] for row in rows if row[-1] == 0 and row[-2] == 0]
csv_writer = csv.writer(open('drows.csv', 'w')).writerows(drows)














# b0rows = [row for row in brows if row[0] == 0 and row[1] == 0]
# csv_writer = csv.writer(open('brows.csv', 'w')).writerows(b0rows)
# b0rows = [row for row in brows if row[0] != 0 and row[1] != 0]
# csv_writer = csv.writer(open('brows.csv', 'w')).writerows(b0rows)
# csv_writer = csv.writer(open('brows.csv', 'w')).writerows(b0rows)
# b0rows = [row[0] - row[1] for row in brows if row[0] != 0 and row[1] != 0]
# csv_writer = csv.writer(open('brows.csv', 'w')).writerows(b0rows)
# b0rows = [[row[0] - row[1]] for row in brows if row[0] != 0 and row[1] != 0]
# csv_writer = csv.writer(open('brows.csv', 'w')).writerows(b0rows)
# b0rows = [row for row in brows if row[0] != 0 and row[1] != 0]
# csv_writer = csv.writer(open('brows.csv', 'w')).writerows(b0rows)
# hist
