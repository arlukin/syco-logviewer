<h>The Syco Logviwer</h1>


<h2>Req</h2>

Apache webbserver
Mysql databas with logs
Syslog stadards logformat in syslog

Syco to generate host list in webpage

</h2>Install</h2>

Copy the www folder containing all www files to /var/www/html/
Copy the apache vhost.conf file in the etc folder to /etc/httpd/cond.d
Make shoure that the mod_cgi.se is enbaled in you apache config /etc/httod/httpd.conf
Set upp user i htacess file ore use ldap read.

Set upp mysql settings in the mysql.py file (User must have read to Syslog database)
Run sql file for mysql config

<h3>SQL User</h3>

GRANT SELECT,INSERT,UPDATE on Syslog.Exclude TO 'rsyslogd'@'localhost';
GRANT SELECT,INSERT,UPDATE on Syslog.alert TO 'rsyslogd'@'localhost';
GRANT SELECT,INSERT,UPDATE on Syslog.signed TO 'rsyslogd'@'localhost';
GRANT SELECT on Syslog.* TO 'rsyslogd'@'localhost';




<h3>Extra nagios monitoring</h3>
Extra: set upp logclean script
Extra: Use nagios to montor logs

Setup upp in webbpage what to exclude and alert in.
"OK" settings will generate alerts if log entory is not find on the host chosen. 

Cleaning out non wanted log entories define with add this script to crontab to run every hour.
mysql_clean_exclude.py

Nagios alert are triggerd with nrpe to run on the script
auto_alert.py 


<h3>Set up ldap to users</h3>
Use ldap instead of htacess file to host files.
Uncomment the ldap section in the vhost.conf file

</h2>Use</h2>
Show daily logs
Sining of logs
Hidning non use logresults
Removing non use logresults
Trigger nagios alert on logs fins i db
Trigger nagios alert on log NOT find in db on host

