from os.path import exists

from connect import *


class Config:
    
    def __init__(self):

      self.config_file = 'connect.py'

      self._local_db_name = None
      self._local_db_host=None
      self._local_db_user=None
      self._local_db_password=None


      #New Host Server
      self._remote_server_ip = None
      self._remote_server_user = None
      self._remote_server_pw = None
      self._remote_server_html_dir = None


      # New Host DB
      self._remote_host_db = None
      self._remote_db_host = None
      self._remote_db_user = None
      self._remote_db_password = None


      print('Config loaded')


    ###############################
    #
    #   Configure Local DB
    #
    ###############################

    # local_db_name
    @property
    def local_db_name(self):

        return self._local_db_name

    @local_db_name.setter
    def local_db_name(self, value):
        self._local_db_name = value

    @local_db_name.deleter
    def local_db_name(self):
        del self._local_db_name


    # local_db_host
    @property
    def local_db_host(self):
        return self._local_db_host

    @local_db_host.setter
    def local_db_host(self, value):
        self._local_db_host = value

    @local_db_host.deleter
    def local_db_host(self):
        del self._local_db_host       


    # local_db_user
    @property
    def local_db_user(self):
        return self._local_db_user

    @local_db_user.setter
    def local_db_user(self, value):
        self._local_db_user = value

    @local_db_user.deleter
    def local_db_user(self):
        del self._local_db_user 


    # local_db_password
    @property
    def local_db_password(self):
        return self._local_db_password

    @local_db_password.setter
    def local_db_password(self, value):
        self._local_db_password = value

    @local_db_password.deleter
    def local_db_password(self):
        del self._local_db_password 




    ###############################
    #
    #   Configure Remote Server Access
    #
    ###############################

    # remote_server_ip
    @property
    def remote_server_ip(self):
        return self._remote_server_ip

    @remote_server_ip.setter
    def remote_server_ip(self, value):
        self._remote_server_ip = value

    @remote_server_ip.deleter
    def remote_server_ip(self):
        del self._remote_server_ip 


    # remote_server_user
    @property
    def remote_server_user(self):
        return self._remote_server_user

    @remote_server_user.setter
    def remote_server_user(self, value):
        self._remote_server_user = value

    @remote_server_user.deleter
    def remote_server_user(self):
        del self._remote_server_user 

    # remote_server_pw
    @property
    def remote_server_pw(self):
        return self._remote_server_pw

    @remote_server_pw.setter
    def remote_server_pw(self, value):
        self._remote_server_pw = value

    @remote_server_pw.deleter
    def remote_server_pwr(self):
        del self._remote_server_pw



    # remote_server_html_dir
    @property
    def remote_server_html_dir(self):
        return self._remote_server_html_dir

    @remote_server_html_dir.setter
    def remote_server_html_dir(self, value):
        self._remote_server_html_dir = value

    @remote_server_html_dir.deleter
    def remote_server_html_dir(self):
        del self._remote_server_html_dir         


    ###############################
    #
    #   Configure Remote DB
    #
    ###############################

    # remote_host_db
    @property
    def remote_host_db(self):
        return self._remote_host_db

    @remote_host_db.setter
    def remote_host_db(self, value):
        self._remote_host_db = value

    @remote_host_db.deleter
    def remote_host_db(self):
        del self._remote_host_db 


    # remote_db_host
    @property
    def remote_db_host(self):
        return self._remote_db_host

    @remote_db_host.setter
    def remote_db_host(self, value):
        self._remote_db_host = value

    @remote_db_host.deleter
    def remote_db_host(self):
        del self._remote_db_host 
    

    # remote_db_user
    @property
    def remote_db_user(self):
        return self._remote_db_user

    @remote_db_user.setter
    def remote_db_user(self, value):
        self._remote_db_user = value

    @remote_db_user.deleter
    def remote_db_user(self):
        del self._remote_db_user 
   

    # remote_db_password
    @property
    def remote_db_password(self):
        return self._remote_db_password

    @remote_db_password.setter
    def remote_db_password(self, value):
        self._remote_db_password = value

    @remote_db_password.deleter
    def remote_db_password(self):
        del self._remote_db_password 



    ###############################
    #
    #   Methods
    #
    ###############################

    def file_exists(self):
      if exists(self.config_file):
        return True
      return False


    def file_is_complete(self):
      if self.file_exists:
        return True
      return False


    def extract_config(self):

      self.local_db_name = LOCAL_DB_NAME
      self.local_db_host = LOCAL_DB_HOST
      self.local_db_user = LOCAL_DB_USER
      self.local_db_password = LOCAL_DB_PASSWORD


      #New Host Server
      self.remote_server_ip = REMOTE_SERVER_IP
      self.remote_server_user = REMOTE_SERVER_USER
      self.remote_server_html_dir = REMOTE_SERVER_HTML_DIR


      # New Host DB
      self.remote_host_db = REMOTE_HOST_DB
      self.remote_db_host = REMOTE_DB_HOST
      self.remote_db_user = REMOTE_DB_USER
      self.remote_db_password = REMOTE_DB_PASSWORD

      print(self.local_db_name)
      print(self.local_db_host)
      print(self.local_db_user)
      print(self.local_db_password)
      return
