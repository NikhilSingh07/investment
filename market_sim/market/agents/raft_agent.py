import random

class RaftAgent:
    
    def __init__(self, agent_id, price_opinion):
        self.agent_id = agent_id
        self.price_opinion = price_opinion
        self.price_log = []

    #-------------------- dummy price: logic is simple, they return their own price opinion
    def propose_price(self):
        return self.price_opinion
    
    #--------------------dummy voting: accepts the proposal 80% of the time
    def vote(self, proposed_price):
        return random.random() < 0.8
    
    #-------------------recording the price in the logs
    def record_price(self, price):
        self.price_log.append(price)

    def get_final_price(self):
        return self.price_log[-1] if self.price_log else self.price_opinion