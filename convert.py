#!/usr/bin/env python
import datetime
import sys
from xml.etree import ElementTree as ET

for filename in sys.argv[1:]:
    with open(filename.rsplit('.', 1)[0] + '.srt', 'w') as output:
        data = ET.parse(filename)
        start_date = datetime.datetime(2013, 1, 1)

        for idx, item in enumerate(data.findall('subtitle')):
            start = float(item.find('start').text.replace(',', '.'))

            start = start_date + datetime.timedelta(0, start)
            end = start_date + datetime.timedelta(0,
                                                  float(item.find('end').text.replace(',', '.')))
            text = item.find('text').text or ''

            print >>output, idx
            print >>output, '{0} --> {1}'.format(
                start.strftime('%H:%M:%S,%f')[0:-3],
                end.strftime('%H:%M:%S,%f')[0:-3]
            )
            print >>output, text.encode('utf-8')
            print >>output

