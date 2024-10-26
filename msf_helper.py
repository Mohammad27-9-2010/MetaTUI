# msf_helper.py
from msfrpc import MsfRpcClient

class MetasploitHelper:
    def __init__(self, password='your_msf_password'):
        # Initialize RPC connection to Metasploit
        self.client = MsfRpcClient(password, ssl=True)

    def get_exploits(self):
        # Retrieve available exploits
        return self.client.modules.exploits

    def execute_command(self, command):
        # Execute a command in Metasploit
        return self.client.call(command)
