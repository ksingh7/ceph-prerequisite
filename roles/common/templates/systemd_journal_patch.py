#!/bin/python
import subprocess

cmd = "journalctl --verify"
restart_journal_service = "False"

p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
out, err = p.communicate()
p_status = p.wait()
if p_status >= 1:
 error_string=err.split()
 for i in range(len(error_string)-1,0,-1):
   temp = error_string[i]
   if temp.find("Bad") > -1 or temp.find("Cannot") > -1:
      remove_journal_log = "rm -rf "+error_string[i-1]
      p = subprocess.Popen(remove_journal_log, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
      restart_journal_service = "True"

if restart_journal_service == "True":
  p = subprocess.Popen(['systemctl','restart',' systemd-journald.service'], stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
  p_status = p.wait()
  out, err = p.communicate()
  if p_status == 0:
    print "Journal logs cleaned"
  else:
    print "There was some error while cleaning journal logs"
    print err
print "Journal patch script completed successfully"
