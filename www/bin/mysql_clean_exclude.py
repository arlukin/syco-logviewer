#!/usr/bin/env python

'''
 DELETE v from SystemEvents v LEFT JOIN Exclude e ON (v.Message LIKE concat('%',e.exclude,'%')) WHERE e.exclude IS NOT NULL AND 
 v.DeviceReportedTime BETWEEN '2012-11-15 00:00:00' AND '2012-11-15 23:59:59' AND e.status = "DELETE";

 '''

#from log_mysql import search_logs
from datetime import date, timedelta
import subprocess
from mysql import mysql_query

def clean_mysql():
	'''
	Cleaning out mysql from delete strings inserted into logadmin site.
	Run every day to clean out from non intressted log enteris.
	'''

	#What date to use for deleteing
	sql="""
	DELETE 
		v 
	from 
		SystemEvents v 
			LEFT JOIN Exclude e ON (v.Message LIKE concat('%',e.exclude,'%')) 
		WHERE 
			e.exclude IS NOT NULL AND  
			v.DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' AND 
		e.status = 'DELETE'""".format(date.today())
	
	#Runningg sql
	mysql_query(sql)
	
	#REMOVE YESTERDAYS LOG ALL
	sql="""
        DELETE
                v
        from
                SystemEvents v
                        LEFT JOIN Exclude e ON (v.Message LIKE concat('%',e.exclude,'%'))
                WHERE
                        e.exclude IS NOT NULL AND
                        v.DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' AND
                e.status = 'DELETE'""".format(date.today() - timedelta(1))

        #Runningg sql
        mysql_query(sql)

	#Logging to syslog
	logthis ="logger -t syco-task -s 'Cleaning logserver mysql from excludes'"
	subprocess.Popen(logthis.split())



def clean_mysql_facilty():
	'''
	Cleaning mysql based on facility
	'''
	sql="delete from SystemEvents where SysLogTag LIKE  'postfix/qmgr%' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' LIMIT 1000;".format(date.today())
	mysql_query(sql)

	sql="delete from SystemEvents where SysLogTag LIKE  'postfix/bounce%' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' LIMIT 1000;".format(date.today())
        mysql_query(sql)
	
	sql="delete from SystemEvents where SysLogTag LIKE  'postfix/cleanup%' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' LIMIT 1000;".format(date.today())
        mysql_query(sql)

	sql="delete from SystemEvents where SysLogTag LIKE  'postfix/pickup%' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' LIMIT 1000;".format(date.today())
        mysql_query(sql)

	sql="delete from SystemEvents where SysLogTag LIKE  'postfix/smtp%' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' LIMIT 1000;".format(date.today())
        mysql_query(sql)

	sql="delete from SystemEvents where SysLogTag LIKE  'postfix/local%' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' LIMIT 1000;".format(date.today())
        mysql_query(sql)
	
	sql="delete from SystemEvents where SysLogTag LIKE  'icinga:' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' LIMIT 1000;".format(date.today())
        mysql_query(sql)

	sql="delete from SystemEvents where SysLogTag LIKE  'slapd[%]:' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' LIMIT 1000;".format(date.today())
        mysql_query(sql)

	sql="delete from SystemEvents where SysLogTag LIKE  '%audispd%:' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' LIMIT 2000;".format(date.today())
        mysql_query(sql)

	sql="delete from SystemEvents where SysLogTag LIKE  'postfix%' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' LIMIT 1000;".format(date.today())
        mysql_query(sql)

	sql="delete from SystemEvents where SysLogTag LIKE  'kernel%' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' LIMIT 1000;".format(date.today())
        mysql_query(sql)

	sql="delete from SystemEvents where SysLogTag LIKE  'ntpd%' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' LIMIT 1000;".format(date.today())
        mysql_query(sql)

	sql="delete from SystemEvents where SysLogTag LIKE  '%cron.daily%' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' LIMIT 1000;".format(date.today())
        mysql_query(sql)

	sql="delete from SystemEvents where SysLogTag LIKE  '%#015%' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' LIMIT 1000;".format(date.today())
        mysql_query(sql)

	sql="delete from SystemEvents where SysLogTag LIKE  '/' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' LIMIT 1000;".format(date.today())
        mysql_query(sql)

	sql="delete from SystemEvents where SysLogTag LIKE  '%cron.hourly%' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' LIMIT 1000;".format(date.today())
        mysql_query(sql)

	sql="delete from SystemEvents where SysLogTag LIKE  '%#00%' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' LIMIT 1000;".format(date.today())
        mysql_query(sql)

	sql="delete from SystemEvents where SysLogTag LIKE  '%nrpe%' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' LIMIT 1000;".format(date.today())
        mysql_query(sql)

	sql="delete from SystemEvents where SysLogTag LIKE  '%sudo%' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' LIMIT 1000;".format(date.today())
        mysql_query(sql)

	sql="delete from SystemEvents where SysLogTag LIKE  'freshclam%' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59' LIMIT 1000;".format(date.today())
        mysql_query(sql)

	# REMOVE YESTERDAYS LOGS ALL OF THEM
	sql="delete from SystemEvents where SysLogTag LIKE  'audispd:' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59'".format(date.today() - timedelta(1))
        mysql_query(sql)

        sql="delete from SystemEvents where SysLogTag LIKE  'kernel%' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59'".format(date.today() - timedelta(1))
        mysql_query(sql)

        sql="delete from SystemEvents where SysLogTag LIKE  'nrpe%:' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59'".format(date.today() - timedelta(1))
        mysql_query(sql)

        sql="delete from SystemEvents where SysLogTag LIKE  'slapd[%]:' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59'".format(date.today() - timedelta(1))
        mysql_query(sql)

	sql="delete from SystemEvents where SysLogTag LIKE  'postfix%' AND DeviceReportedTime BETWEEN '{0} 00:00:00' AND '{0} 23:59:59'".format(date.today() - timedelta(1))
        mysql_query(sql)

	#Logging to syslog
        #logthis ="logger -t syco-task -s 'Cleaning from log facility'"
        #subprocess.Popen(logthis.split())

clean_mysql()
clean_mysql_facilty()	
