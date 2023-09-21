import subprocess
from ImcSdk import ImcHandle

user = "admin"
password = "P@ssw0rd!23"

servers = []
with open('../iplist.csv', 'r') as file:
    servers = file.read().splitlines()

hostname = ""
with open('../hostname.csv', 'r') as file:
    hostname = file.read().strip()

handle = ImcHandle()
handle.login(servers[0], user, password)

handle.set_imc_ntp_server(ntp_enable="yes", ntp_server1="1.1.1.2", force=True)

handle.set_imc_mgmt_interface_dns_alternate(dns_alternate="10.1.1.1", force=True)
handle.set_imc_mgmt_interface_dns_preferred(dns_preferred="10.2.2.2", force=True)
handle.set_imc_mgmt_interface_hostname(hostname=hostname, force=True)

handle.set_imc_top_system(timezone="America/Los_Angeles", force=True)

handle.logout()
