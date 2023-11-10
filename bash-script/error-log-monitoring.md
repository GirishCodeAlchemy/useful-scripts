# Apache Error Log Monitoring

## Overview

This guide provides steps to monitor Apache error logs on a Linux system and receive email notifications when the logs contain the word "error."

## Step-by-Step Instructions

### Step 1: Locate Apache Error Log

Locate the Apache error log file on your system. Update the `ErrorLog` directive in your Apache configuration file to the desired log file path. For example:

```plaintext
/var/log/apache2/error.log
```

### Step 2: Locate Apache Error Log

Ensure that the mailx utility is installed on your system. You can install it using your package manager.

### Step 3: Locate Apache Error Log

Create a monitoring script, e.g., monitor.sh, with the following content:

```bash
#!/bin/bash
if grep -q "error" /var/log/apache2/error.log; then
    echo "Apache error detected in error log." | mail -s "Apache Error Notification" user1@gmail.com
fi
```

Make the script executable:

```bash
chmod +x monitor.sh
```

### Step 4: Set Up Cron Job

Edit the crontab for the current user:

```bash
crontab -e
```

Add an entry to run your monitoring script at the desired interval. For example, to check every minute:

```plaintext
* * * * * /path/to/monitor.sh
```
