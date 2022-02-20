from DB import *
from Server import *
from Config import *


config = Config()
local_db = DB()
#remote_db = DB()
wp = WP()

if config.file_exists() and config.file_is_complete():

  # Extract Confguration File
  config.extract_config()

  # Copy wp-config.php file --> wp-config.local.php
  wp_config_backed_up = wp.backup_wp_config()
  live_wp_cinfig_created =wp.create_live_wp_config()

  if wp_config_backed_up and live_wp_config_created :

    local_db_exported = local_db.export_db()

    if local_db_exported:

      # upload db file

      # upload wordpress files

    else:
      print('Failed to export Wordpress database on local machine.  Please check that the credentials are correct')

  else:
    print('Failed to create wp_config.php file.  Please make sure the wp_config.php file has read and write permissions')


  # Connect to Server
  server = Server(config)

  server.connect("ls -l")


  #server.copy_files()

  print('Config file exists')

else:
  print('No config file... boo!')
#  Config.askQuestions()





# Hey all!  Welcome to WP-Migrator!  Created in order to help you facilitate the Wordpress migration process.  Built out of my own need to migrate a rather large Wordpress site, before using this app you should have the following information available and priveleges:
# On you localhost or current wordpress environment:
# - Server Name/IP (localhost, an ip address, etc...)
# - The database name where wordpress is installed
# - The user who has access to the database
# - The password of said user who has access to the database
#
# On the server where your wordpress will be migrated to:
# - Ability to access via SSH (Port 22 Open)
# - IP address of server
# - Username to login to server
# - Web directory where wordpress is to be installed (ex. /var/www/public_html, /var/www/public_html)
# - Hostname/IP of database server
# - The user who has access to the database
# - The password of said user who has access to the database
#
#   You can also edit the connect.py configuration file in this directory to populate this information ahead of time!  Anywho, lets get to it shall we!
#
#

# Enter localhost db connection details
# Host: (defaults to localhost)
# User: (defaults to root)
# Password:
# Database Name

# Great!  Now lets talk about your new host!
# What is the domain of your new host? (ex. https://www.mywebsite.com)
# What is the name of the database on your new server/host?
# What is the username for your newly created database on your new server?
# What is the password for this user?

# What is the hostname where your database is located ? (This is usually "localhost" if on the same server or an IP address if otherwise)

# Connect to localhost DB where wordpress database is

# Export all tables individually into folder (db)

# cahnge all "localhost" variables to "domain" in specific db_table files

# Update wp-config.php file to include "prod" database details
