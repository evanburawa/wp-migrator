from paramiko import SSHClient
from scp import SCPClient


class Server:
    
    def __init__(self, config):
      self.config = config

      self._host = config.remote_server_ip
      self._user = config.remote_server_user
      self._pw = config.remote_server_pw
      self._html_dir = config.remote_server_html_dir

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



    ###############################
    #
    #   Methods
    #
    ###############################

    def connect():
      return


    def upload_files():
      return