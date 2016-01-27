#quotesagram.py
#the best quote sharing service

class Quote(object):

        def __init__(self,quote_text, user_posted, location, num_likes):
                self.quote_text = quote_text
                self.user_posted = user_posted
                self.location = location
                self.num_likes = num_likes

        def like(self):
                self.num_likes = self.num_likes + 1

        def unlike(self):
                slef.num_likes = self.num_likes - 1

        def show_quote(self):
                print("U:" + user_posted)
                print("L:" + location)
                print("Quote:" + quote_text)
                print("Likes:" + str(num_likes))


X = Quote("Nothing with Shawn." , "kevin_is_cool" , "San Fransico" , 0)
