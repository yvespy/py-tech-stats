from matplotlib import pyplot as plt


def build_chart(data: list[tuple], output_path: str) -> None:
    name, count = zip(*data)
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(name, count, color='skyblue', edgecolor='black', width=0.6)
    ax.bar_label(bars, fontsize=10, fontweight='bold', padding=3)
    plt.xticks(rotation=45, ha='right')

    ax.set_title("Top tech skills on market", fontsize=14, fontweight='bold')
    ax.set_xlabel("Tech Category", fontsize=12)
    ax.set_ylabel("Quantity of mentions", fontsize=12)

    ax.set_axisbelow(True)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    return None
