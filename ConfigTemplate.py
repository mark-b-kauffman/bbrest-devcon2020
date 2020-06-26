# ConfigTemplate.py
# Copy to Config.py. Modify values with what you got from 
# your REST App registration on developer.blackboard.com
# Use:
# import Config
# KEY = Config.config['learn_rest_key']
# SECRET = Config.config['learn_rest_key']
# etc...
config = {
    "verify_certs" : "True",
    "learn_rest_fqdn" : "YOURLEARNSERVER_Fully_Qualified_Domain_Name",
    "learn_rest_key" : "YOURLEARNRESTKEY",
    "learn_rest_secret" : "YOURLEARNRESTSECRET",
    "app_url" : "YOURAPPURLWITHHTTPS"
}

