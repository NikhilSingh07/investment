import random

"""
 Goals: > From a set of agents elect a random leader
        > Leader proposes a new price for market
        > Other agents vote to approve or reject the proposal
        > If majority is "yes" consensus is reached and proposal price is accepted
"""


class RaftConsensus:

    #---------------------List of participating agents
    def __init__(self, agents):
        self.agents = agents  

    #--------------------Electing a random leader   
    def elect_leader(self):
        return random.choice(self.agents)
    
    #-------------------Leader proposes a price based on current price
    def propose_price(self, leader):
        #------------------calling propose_price method from raft_agent class
        return leader.propose_price()

    def reach_consensus(self, proposed_price, leader):
        votes = []
        for agent in self.agents:
            if agent != leader:
                #-------------------------------- Ask each non-leader agent to vote
                votes.append(agent.vote(proposed_price))
        yes_votes = sum(votes)  # --------------1 is yes 0 is no

        #----------------------------------Returning majority's decision
        return yes_votes >= len(self.agents) // 2