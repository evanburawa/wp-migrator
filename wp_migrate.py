from DB import *
from Server import *
from Config import *


config = Config()

if config.file_exists() and config.file_is_complete():

  # Extract Confguration File
  config.extract_config()

  # Connect to Server
  server = Server(config)
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
