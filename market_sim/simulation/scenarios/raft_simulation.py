from market.agents.raft_agent import RaftAgent
from market.dynamics.price_consensus import run_price_consensus

"""
Running simple simulation of market price consensus using Raft-like voting, where multiple agents propose
and agree on a new price in each round.

It simulates 10 rounds of price consesus using raft algorithm.

  > Elect a leader each round
  > Propose a new market price
  > Vote to reach consensus
  > Update the price if a majority agrees



"""

def run_raft_simulation():

    #----------------Initialising 5 trading agents
    agents = [RaftAgent(f"Agent {i+1}") for i in range(5)]
    current_price = 100.0


    #----------------Running simulation for 10 rounds
    for round_num in range(10):
        print(f"\n🌀 Round {round_num + 1}")

        #-------------Performing a single round of price consensus
        consensus_price = run_price_consensus(agents, current_price)

        print(f"Agreed Price: {consensus_price}")