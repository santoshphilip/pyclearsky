# Copyright (c) 2013 Santosh Philip

# This file is part of pyclearsky.

# pyclearsky is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# pyclearsky is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with pyclearsky.  If not, see <http://www.gnu.org/licenses/>.

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
