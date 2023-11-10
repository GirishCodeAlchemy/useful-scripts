# useful-scripts

## Cronjob

- [Error Log Detection](bash-script/error-log-monitoring.md): Set up a cronjob to monitor the error.log file for occurrences of "error" and receive email notifications.

## Bash Scripts

- [Monitor Server Ports and Alert](bash-script/monitor-server-ports-and-notify.sh): Continuously monitors server ports. Sends email notifications if any new listening ports are detected.

- [Prompt Folder Path and Download Package](bash-script/prompt-folder-path-and-download-package.sh): Prompts for a folder path. Indicates folder existence and creates the folder if it doesn't exist. Downloads and installs a package in the newly created folder.

- [Restart Server](bash-script/restart-server.sh): Shell script to monitor a process (e.g., Tomcat) every minute. If the process stops, it should restart; otherwise, it exits.

- [Docker Restart](bash-script/docker-container-restart.sh): Shell script to monitor Docker containers. If the containers exit, they should restart automatically.
