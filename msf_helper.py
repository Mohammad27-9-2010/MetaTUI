# msf_helper.py
import os
from pymetasploit3.msfrpc import MsfRpcClient

class MetasploitHelper:
    def __init__(self):
        self.client = MsfRpcClient(os.getenv("MSF_PASSWORD"), ssl=True)

    def get_exploits(self):
        # Retrieve available exploits
        return self.client.modules.exploits

    def execute_command(self, command):
        # Execute a command in Metasploit
        return self.client.call(command)
