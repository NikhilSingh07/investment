import random

class RaftAgent:
    
    def __init__(self, name):
        self.name = name  #identifier for the agent
        self.price_log = []   # empty price logs

    #-------------------- dummy price: logic is simple, slightly changing from current price
    def propose_price(self, current_price):
        return round(current_price + random.uniform(-2.0, 2.0), 2)
    
    #--------------------dummy voting: accepts the proposal 80% of the time
    def vote(self, proposed_price):
        return random.random() < 0.8
    
    #-------------------recording the price in the logs
    def record_price(self, price):
        self.price_log.append(price)