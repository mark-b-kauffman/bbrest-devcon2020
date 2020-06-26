from bbrest import BbRest
key = "4987dYOUR_KEY____HERE_NOT_MINE7c31bc"
secret = "kLCv_YOUR_SECRET_HERE_L19XmtjC8L"
learnfqdn = "kauffman380011.ddns.net"
bb = BbRest(key, secret, f"https://{learnfqdn}")  # Does a lot! Get the system version, pull in the functions from dev portal, 2-legged authentication w/ caching of token."
print(bb.expiration())
