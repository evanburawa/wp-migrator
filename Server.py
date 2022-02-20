"""Client to handle connections and actions executed against a remote host."""
from os import system
from dotenv import load_dotenv
from typing import List

from paramiko import SSHClient, AutoAddPolicy, RSAKey
from paramiko.auth_handler import AuthenticationException, SSHException
from scp import SCPClient, SCPException
# from log import logger
import logging


class Server:
    
    def __init__(self, config):

      self.config = config

      self._host = config.remote_server_ip
      self._user = config.remote_server_user
      self._pw = config.remote_server_pw
      self._ssh_key_filepath = config.ssh_key_filepath
      self._html_dir = config.remote_server_html_dir

      self._wp_folder_path = None;
      self.client = None



      print('Server loaded')


    # host
    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        self._host = value

    @host.deleter
    def host(self):
        del self._host


    # user
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @user.deleter
    def user(self):
        del self._user


    # pw
    @property
    def pw(self):
        return self._pw

    @pw.setter
    def pw(self, value):
        self._pw = value

    @pw.deleter
    def pw(self):
        del self._pw


    # html_dir
    @property
    def html_dir(self):
        return self._html_dir

    @html_dir.setter
    def html_dir(self, value):
        self._html_dir = value

    @html_dir.deleter
    def html_dir(self):
        del self._html_dir

    # ssh_key_filepath
    @property
    def ssh_key_filepath(self):
        return self._ssh_key_filepath

    @ssh_key_filepath.setter
    def ssh_key_filepath(self, value):
        self._ssh_key_filepath = value

    @ssh_key_filepath.deleter
    def html_dir(self):
        del self._ssh_key_filepath



    ###############################
    #
    #   Methods
    #
    ###############################

    def _get_ssh_key(self):
        """ Fetch locally stored SSH key."""
        try:
            self.ssh_key = RSAKey.from_private_key_file(
                self.ssh_key_filepath
            )
            logging.info(
                f"Found SSH key at self {self.ssh_key_filepath}"
            )
            return self.ssh_key
        except SSHException as e:
            logging.error(e)


    def _upload_ssh_key(self):
        try:
            system(
                f"ssh-copy-id -i {self.ssh_key_filepath}.pub {self.user}@{self.host}>/dev/null 2>&1"
            )
            logging.info(f"{self.ssh_key_filepath} uploaded to {self.host}")
        except FileNotFoundError as error:
            logging.error(error)


    @property
    def connect(self):
        """Open connection to remote host. """
        try:
            client = SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(AutoAddPolicy())
            client.connect(
                self.host,
                username=self.user,
                password=self.pw,
                key_filename=self.ssh_key_filepath,
                timeout=5000,
            )
            
            print('Connected!')
            stdin, stdout, stderr = client.exec_command("pwd")
            lines = stdout.readlines()
            print(lines)

            return client
        except AuthenticationException as e:
            logging.error(
                f"Authentication failed: did you remember to create an SSH key? {e}"
            )
            raise e


    def run_command(self, cmd):
        ssh = self.connect()
        stdin, stdout, stderr = ssh.exec_command(command)
        lines = stdout.readlines()
        print(lines)


    def disconnect(self):
        """Close ssh connection."""
        if self.client:
            self.client.close()
        if self.scp:
            self.scp.close()


    @property
    def scp(self) -> SCPClient:
        conn = self.connection
        return SCPClient(conn.get_transport())


    def execute_commands(self, commands: List[str]):
        """
        Execute multiple commands in succession.
        :param commands: List of unix commands as strings.
        :type commands: List[str]
        """
        for cmd in commands:
            stdin, stdout, stderr = self.client.exec_command(cmd)
            stdout.channel.recv_exit_status()
            response = stdout.readlines()
            for line in response:
                logging.trace(f"INPUT: {cmd}")
                logging.info(f"OUTPUT: {line}")


    def bulk_upload(self, files: List[str]):
        """
        Upload multiple files to a remote directory.

        :param files: List of local files to be uploaded.
        :type files: List[str]
        """
        try:
            self.scp.put(files, remote_path=self.remote_path)
            LOGGER.info(
                f"Finished uploading {len(files)} files to {self.remote_path} on {self.host}"
            )
        except SCPException as e:
            raise e


    def upload_files(self):
      return