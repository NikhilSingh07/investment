from simulation.scenarios.raft_simulation import run_raft_simulation

def test_raft_simulation_runs():

    # Run the simulation and capture results
    result = run_raft_simulation()

    # Ensure the simulation completed
    assert result is not None, "Simulation did not return any result"

    # Check that a leader was elected
    assert result.get("leader_id") is not None, "No leader was elected"

    # Check that a consensus price was agreed
    assert result.get("consensus_price") is not None, "No consensus price was reached"

    # Check that all agents agreed on the price
    agent_prices = result.get("agent_prices", [])
    assert all(price == result["consensus_price"] for price in agent_prices), "Agents did not agree on the same price"