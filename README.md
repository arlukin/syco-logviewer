<h>The Syco Logviwer</h1>


<h2>Req</h2>

Apache webbserver
Mysql databas with logs
Syslog stadards logformat in syslog

Syco to generate host list in webpage

</h2>Install</h2>

Copy the ww folder containing all www files to /var/www/html/
Copy the apache vhost.conf file in the etc folder to /etc/httpd/cond.d
Set upp mysql settings in the log_mysql.py file (User must have read to Syslog database)
Run sql file for mysql config
Extra: set upp logclean script
Extra: Use nagios to montor logs


Setup upp in webbpage what to exclude and alert in.
"OK" settings will generate alerts if log entory is not find on the host chosen. 

Cleaning out non wanted log entories define with add this script to crontab to run every hour.
mysql_clean_exclude.py

Nagios alert are triggerd with nrpe to run on the script
auto_alert.py 


</h2>Use</h2>
Show daily logs
Sining of logs
Hidning non use logresults
Removing non use logresults
Trigger nagios alert on logs fins i db
Trigger nagios alert on log NOT find in db on host

