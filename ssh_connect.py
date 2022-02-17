import paramiko
import ipaddress
command = "df"

# Update the next three lines with your
# server's information

#host = ipaddress.ip_address('192.168.82.69')
host = 'host_ip'
username = 'user'
password = 'password'
port = 22


client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password, port=port)
_stdin, _stdout,_stderr = client.exec_command("df")
print(stdout.read().decode())
data = stdout.read() + stderr.read()
client.close()
