from simulation.scenarios.raft_simulation import run_raft_simulation

def test_raft_simulation_runs():
    try:
        run_raft_simulation()
        assert True
    except Exception as e:
        assert f"Simulation failed: {e}"

        