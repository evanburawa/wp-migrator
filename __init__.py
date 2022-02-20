"""Perform tasks against a remote host."""
from typing import List

#from config import LOCAL_FILE_DIRECTORY

from Server import *
#from .client import RemoteClient
#from .files import fetch_local_files

def execute_command_on_remote(
    ssh_remote_client: Server, commands: List[str] = None
):
    """
    Execute UNIX command on the remote host.
    :param ssh_remote_client: Remote server.
    :type ssh_remote_client: RemoteClient
    :param commands: List of commands to run on remote host.
    :type commands: List[str]
    """
    ssh_remote_client.execute_commands(commands)