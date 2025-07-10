import matplotlib.pyplot as plt

def visualise_raft_result(result):
    initial = result["initial_opinions"]
    final = result["agent_prices"]
    consensus_price = result["consensus_price"]
    agent_ids = [f"Agent_{i+1}" for i in range(len(initial))]

    x = range(len(agent_ids))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot initial and final prices
    ax.bar(x, initial, width, label="Initial Price", color="skyblue")
    ax.bar([i + width for i in x], final, width, label="Final Price", color="lightgreen")

    # Horizontal line for consensus
    ax.axhline(consensus_price, color="red", linestyle="--", label=f"Consensus Price ({consensus_price})")

    # Labels
    ax.set_xlabel("Agents")
    ax.set_ylabel("Price")
    ax.set_title("Raft Consensus: Agent Price Convergence")
    ax.set_xticks([i + width/2 for i in x])
    ax.set_xticklabels(agent_ids, rotation=45)
    ax.legend()

    plt.tight_layout()
    plt.show()
