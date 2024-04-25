#!/bin/bash

EMAIL_TO="your.email@example.com"
EMAIL_SUBJECT="Tomcat Monitor Notification"

PROCESS_NAME="tomcat"

while true; do
 # Check if the process is running
 if pgrep -x "$PROCESS_NAME" >/dev/null; then
  echo "$PROCESS_NAME is running."
 else
  echo "$PROCESS_NAME is not running. Starting it..."

  /path/to/tomcat/bin/startup.sh
  echo "Tomcat was restarted on $(date)" | mail -s "$EMAIL_SUBJECT" "$EMAIL_TO"
 fi
 sleep 60
done

# To sent an email from linux, we can follow below steps:
# https://www.notion.so/Mailx-094034c4261b401a8c31bf7fbe447b7b?pvs=4