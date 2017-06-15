# dynBoto
Short Description:
A simply script to dynamically change Route 53 Records

Description: 
This script goes through a list of user defined subdomains. If those subdomains have an ip which differs from the external IP
of the computer running this script, dynBoto will update the Route53 records for those domains.

Usage:
1) You must install and configure the AWS-CLI software with the creditanls for the Route53 account you wish to update with this script.
2) You must install the boto3 library for python.
3) In the directory where dynBoto.py is saved create a text file called 'subdomains' WITH NO EXTENSION
4) Change HostedZoneId on line 25 & 56 to match the desired hosted zone ID.
5) Change .YOURURL.HERE to your domain name on line 34. 
5) Optional: Set a cron to run this script at your desired interval, for thirty minutes do this....
*/30 * * * * /PATH/TO/PYTHON /PATH/TO/THIS/SCRIPT/dynBoto.py

My cron on debian looks like this...
*/30 * * * * /usr/bin/python /PATH/TO/THIS/SCRIPT/dynBoto.py
