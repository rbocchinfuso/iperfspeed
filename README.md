# iPerf Bandwidth Monitor
Python wrapper to run iPerf tests and log results and send alerts based on performance falling below an expected bandwidth threshold.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
* [iperf3](https://iperf.fr/iperf-download.php)
* [Python 3: I recommend the Anaconda Pyton distrobution](https://www.anaconda.com/distribution/)
* [iperf3](https://pypi.org/project/iperf3/), [pushover_complete](https://pypi.org/project/pushover_complete/), [isstreamer](https://pypi.org/project/ISStreamer/) Python libraries
* [Inital State account and bucket](https://www.initialstate.com/)
* [Pushover account](https://pushover.net/)

##### Notes
*  Client = The machine you have this code on.
*  Server = The machine you will be using as the target for testing.

##### Install iperf3 on client and server
* Debian based distros:```apt-get install iperf3```
* RHEL based distros:  ```yum -Uvh iperf3```
* Other:  _Download the binary from [iperf3](https://iperf.fr/iperf-download.php) site_

##### Install the required Pyton libraries on the client 
```
pip install -r requirements.txt
```

### Configuration
* Modify  pushover.py (only used to test Pushover alerts)
* Copy iperfspeed_config_sample.py to iperfspeed_config.py
```
cp ./iperfspeed_config_sample.py ./iperfspeed_config.py
```
* Modify iperfspeed_config.py

## Testing
* Start iperf3 on server:  ```iperf3 -s```
* Test iperf3 client to server connection from cli:  ```iperf3 -c [IP | HOSTNAME]```
* Test Pushover notifications: ```python test_pushover.py```
* Test iperfspeed.py:  ```python iperfspeed.py```
* Test iperfspeed as background process:  

## Deployment
* Create a cron job entry for iperfspeed_keepalive.sh
```
*/5 * * * * ./iperfspeed_keepalive.sh
```
## Built With
* [Codeanywhere](https://codeanywhere.com/) - Cloud IDE
* [Anaconda](https://www.anaconda.com/distribution/) - Python 3.7 Distrobution
* [Pushover](https://pushover.net/) - Simple Notifications for Android, iOS, and Desktop
* [Initlastate](https://www.initialstate.com/) - Data Streaming + Data Visualizations
* [iPerf3](https://iperf.fr/iperf-download.php) - The ultimate speed test tool for TCP, UDP and SCTP

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request ツ

## History
* version 1 (initial release) - 2019/08/05

## Todo
* Add source process identifier to payload to allow for multi-threaded testing and logging.
* Add tweet to service provider on bandwidth threshold violation.

## Meta
Richard J. Bocchinfuso – [@rbocchinfuso](https://twitter.com/rbocchinfuso) – rbocchifuso@gmail.com

Distributed under the MIT License. See ``License`` for more information.

[https://github.com/rbocchinfuso/](https://github.com/rbocchinfuso/)

## License
MIT License

Copyright (c) [2019] [Richard J. Bocchinfuso]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
