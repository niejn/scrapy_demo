import time
import os
import ntplib
try:

    client = ntplib.NTPClient()
    response = client.request('pool.ntp.org')
    os.system('date ' + time.strftime('%m%d%H%M%Y.%S', time.localtime(response.tx_time)))
except Exception as e:
    print(e)
    print('Could not sync with time server.')

print('Done.')