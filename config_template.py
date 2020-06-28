# config_template.py
# Copy to config.py. Modify values with what you got from 
# your REST App registration on developer.blackboard.com
# Use:
# from config import ict
# KEY = ict['learn_rest_key']
# SECRET = ict['learn_rest_key']
# etc...
ict = {
    "verify_certs" : "True",
    "learn_rest_fqdn" : "YOURLEARNSERVER_Fully_Qualified_Domain_Name",
    "learn_rest_key" : "YOURLEARNRESTKEY",
    "learn_rest_secret" : "YOURLEARNRESTSECRET",
    "app_url" : "YOURAPPURLWITHHTTPS"
}

