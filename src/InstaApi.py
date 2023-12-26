from instagrapi import Client
 
from instagrapi import Client

class IntaApid:
    def __init__(self):
        self.cl = Client()
        self.cl.login_by_sessionid("63677391108%3ALJ8obyTS36mSVe%3A12%3AAYeOSuP2n-3Eaguy6FD3fWuwxyNyJidihIcUs06qmg")
        print(self.cl.user_info(self.cl.user_id))