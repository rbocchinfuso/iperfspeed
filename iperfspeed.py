#!/home/cabox/.pyenv/versions/3.7.0/bin/python
# iperfspeed.py
# Bandwidth Monitor
# RJB - 20190801

import iperf3
import csv
import time
import datetime
from pushover_complete import PushoverAPI
from ISStreamer.Streamer import Streamer
from iperfspeed_config import *

while True:
    c = iperf3.Client()
    c.duration = iperf_duration
    c.server_hostname = iperf_server
    c.port = iperf_port
    c.num_streams = iperf_streams
    c.protocol = iperf_protocol

    print('Connecting to {0}:{1}'.format(c.server_hostname, c.port))
    result = c.run()

    if result.error:
        print(result.error)
    else:
        print('')
        print('Test completed:')
        print('  started at         {0}'.format(result.time))
        print('  transmitted (MB)    {0:,.2f}'.format(result.sent_bytes/1000000))
        print('  avg cpu load       {0:,.2f}%\n'.format(result.local_cpu_total))

        print('Average transmitted data in various formats:')
        print('  bits per second      (bps)   {0:,.2f}'.format(result.sent_bps))
        print('  Kilobits per second  (kbps)  {0:,.2f}'.format(result.sent_kbps))
        print('  Megabits per second  (Mbps)  {0:,.2f}'.format(result.sent_Mbps))
        print('  KiloBytes per second (kB/s)  {0:,.2f}'.format(result.sent_kB_s))
        print('  MegaBytes per second (MB/s)  {0:,.2f}'.format(result.sent_MB_s))

        if result.sent_MB_s < transfer_min or test_run:
            # send alert to pushover
            p = PushoverAPI(p_apptoken)  # an instance of the PushoverAPI representing your application
            # send a message to a user
            p.send_message(p_userkey,
                           'iPerf Speed Warning\n' +
                            'date:\t\t{:%Y-%m-%d}\n'.format(datetime.datetime.now()) +
                            'time:\t\t{:%H-%M}\n'.format(datetime.datetime.now()) +
                            'CPU utilization :\t\t%d%%\n' % (result.local_cpu_total) +
                            'transmitted:\t\t%d MB/s\n' % (result.sent_bytes/1000000) +
                            'throughput:\t\t%d Mb/s\n' % (result.sent_MB_s)
                            )

    # log stats to local csv file
    with open('stats.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([result.time,
                         '{0:,.2f}'.format(result.sent_bytes/1000000),
                         '{0:,.2f}'.format(result.local_cpu_total),
                         '{0:,.2f}'.format(result.sent_bps),
                         '{0:,.2f}'.format(result.sent_kbps),
                         '{0:,.2f}'.format(result.sent_Mbps),
                         '{0:,.2f}'.format(result.sent_kB_s),
                         '{0:,.2f}'.format(result.sent_MB_s)])

    # create a initalstate streamer instance
    streamer = Streamer(bucket_name=is_bucket_name, bucket_key=is_bucket_key, access_key=is_access_key)

    # send stats to initial state
    streamer.log('transmitted (MB)', '{0:,.2f}'.format(result.sent_bytes/1000000))
    streamer.log('CPU utilization (%)', '{0:,.2f}'.format(result.local_cpu_total))
    streamer.log('throughput (bps)', '{0:,.2f}'.format(result.sent_bps))
    streamer.log('throughput (kbps)', '{0:,.2f}'.format(result.sent_kbps))
    streamer.log('throughput (Mbps)', '{0:,.2f}'.format(result.sent_Mbps))
    streamer.log('throughput (kB/s)', '{0:,.2f}'.format(result.sent_kB_s))
    streamer.log('throughput (MB/s)', '{0:,.2f}'.format(result.sent_MB_s))

    # flush and close the stream
    streamer.close()
