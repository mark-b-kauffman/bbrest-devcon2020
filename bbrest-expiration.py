from bbrest import BbRest
import Config
key = Config.dict['learn_rest_key']
secret = Config.dict['learn_rest_secret']
learnfqdn = Config.dict['learn_rest_fqdn']
bb = BbRest(key, secret, f"https://{learnfqdn}")  # Does a lot! Get the system version, pull in the functions from dev portal, 2-legged authentication w/ caching of token."
print(bb.expiration())
