from subprocess import PIPE, Popen


def popen(command):
    p = Popen([command], shell=True, stdout=PIPE, stderr=PIPE)
    op = p.communicate()
    stdout = (op[0].decode("utf -8"))
    stderr = (op[1].decode("utf -8"))
    return (stdout, stderr)

def sshCommand(command, host)
    p_command = f'ssh {host} "{command}"'
    p = Popen([p_command], shell=True, stdout=PIPE, stderr=PIPE)
    op = p.communicate()
    stdout=(op[0].decode("utf -8"))
    stderr = (op[1].decode("utf -8"))
    return (stdout, stderr)

def port_check(host, port):
    result = popen(f"nc -zv {host} {port}")
    if (result[-1].count("succeeded!") > 0):
        return "Success"
    else:
        return "Failure"


response = port_check("localhost", 8080)
print(response)
