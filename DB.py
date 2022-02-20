class DB:
    
    def __init__(self, config, server):

      # Instance of Server (to allow for access to run mysql commands on remote server)
      self.server = server

      self._host = config._db_host
      self._user = config._db_user
      self._pw = config._db_password
      self._port = config._db_port
      self._db = config._db_name

      print('DB loaded')

    def set_host(host):
      return 

    def set_db_name(db):
      return

    def set_user(user):
      return

    def set_pw(pw):
      return


    def connect():
      return

    def export_db():
      return