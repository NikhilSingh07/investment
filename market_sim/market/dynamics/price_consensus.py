from blockchain.consensus.raft import RaftConsensus

"""
This function executes a single round of price consensus using the Raft algorithm:
   >  Electing a leader from a group of agents.
   >  Having the leader propose a new price.
   >  Asking other agents to vote on the proposed price.
   >  Updating the price only if a majority agree.
"""

def run_price_consensus(agents):

    #------------------Initialize Raft consensus with all agents 
    raft = RaftConsensus(agents)

    #------------------Electing a leader
    leader = raft.elect_leader()

    #------------------Proposing a price
    new_price = raft.propose_price(leader)

    #-----------------Updating the price in the logs if majority agrees
    if raft.reach_consensus(new_price, leader):
        for agent in agents:
            agent.record_price(new_price)
        return new_price, leader.agent_id
    else:
        return leader.price_opinion, leader.agent_id  # No consensus