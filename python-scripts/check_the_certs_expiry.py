import subprocess
from datetime import datetime

# Helper to run SSH and OpenSSL commands
def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

# 1. Get expiry date from certificate
expiry_command = "ssh -q -T -o StrictHostKeyChecking=no confluent@i 'openssl x509 -in /opt/confluent/etc/confluent-security/*.cer -enddate -noout'"
expiry_output = run_command(expiry_command)

# Parse the expiry date from the command output
expiry = expiry_output.split('=')[1].strip()

# 2. Convert expiry date to timestamp
expiry_date = datetime.strptime(expiry, '%b %d %H:%M:%S %Y %Z')  # Parse to datetime object
now_date = datetime.now()

# 3. Calculate the days until expiry
expiry_days = (expiry_date - now_date).days

# 4. Get certificate serial number
serial_command = "ssh -q -T -o StrictHostKeyChecking=no confluent@i 'openssl x509 -text -in /opt/confluent/etc/confluent-security/*.cer | grep -A1 Serial | tail -1'"
cert_sno = run_command(serial_command)

# 5. Log the output
_log = "/path/to/logfile.log"
with open(_log, 'a') as log_file:
    log_file.write(f"{i:<10} | {expiry:<20} | {expiry_days:<10} | {cert_sno:<35}\n")

print(f"Expiry Date: {expiry}")
print(f"Expiry in Days: {expiry_days}")
print(f"Certificate Serial Number: {cert_sno}")
