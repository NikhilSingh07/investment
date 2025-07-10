from market_sim.market.agents.raft_agent import RaftAgent
from market_sim.market.dynamics.price_consensus import run_price_consensus
from market_sim.analysis.visualisation.visualise_raft_results import visualise_raft_result

"""
Running a simulation of market price consensus using Raft-like voting, where multiple agents propose
and agree on a new price in each round.

It simulates 10 rounds of price consesus using raft algorithm.

  > Elect a leader from the agents/candidates
  > Propose a new market price
  > Vote to reach consensus
  > Update the price if a majority agrees

"""

def run_raft_simulation():

    #----------------List of agents with price_opinions
    agents = [
        RaftAgent(agent_id=1, price_opinion=8.5),
        RaftAgent(agent_id=2, price_opinion=10.0),
        RaftAgent(agent_id=3, price_opinion=12.0),
        RaftAgent(agent_id=4, price_opinion=11.0),
        RaftAgent(agent_id=5, price_opinion=9.5),
    ]

    intial_opinions = []

    for agent in agents:
      intial_opinions.append(agent.price_opinion) 

    agent_prices = []

    consensus_price, leader_id = run_price_consensus(agents)

    for agent in agents:
        agent_prices.append(agent.get_final_price())

    return {
        "initial_opinions": intial_opinions,
        "consensus_price": consensus_price,
        "leader_id": leader_id,
        "agent_prices":agent_prices
    }    

if __name__ == "__main__":
    result = run_raft_simulation()
    print("intial_opinions:", result["initial_opinions"])
    print("Consensus Price:", result["consensus_price"])
    print("Leader ID:", result["leader_id"])
    print("Agent Prices:", result["agent_prices"])
    visualise_raft_result(result)
