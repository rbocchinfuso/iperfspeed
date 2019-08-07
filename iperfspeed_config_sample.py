#!/home/cabox/.pyenv/versions/3.7.0/bin/python
# iperfspeed_config.py
# Bandwidth Monitor Config
# RJB - 20190801

# set all configuration parameters here
# min download bandwith (MB/s)
transfer_min = 20
# test = True | production = False
test_run = True
# Pusover User Key
p_userkey = 'ENTER USER KEY'
# Pushover Application API key
p_apptoken = 'ENTER APP TOKEN'
# initalstate variables
is_bucket_name = 'ENTER BUCKET NAME'
is_bucket_key = 'ENTER BUCKET KEY'
is_access_key = 'ENTER ACCESS KEY'
# iPerf settings
iperf_duration = 10
iperf_server = '127.0.0.1'
iperf_port = 5201
iperf_streams = 1
iperf_protocol = 'tcp'
