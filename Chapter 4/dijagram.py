import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_diagram():
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_xlim(-1, 12)
    ax.set_ylim(0, 11)
    ax.axis('off')

    def add_box(x, y, text, color='lightblue'):
        width, height = 3.8, 1.2
        box = patches.FancyBboxPatch((x, y), width, height,
                                     boxstyle='round,pad=0.4', 
                                     edgecolor='black',
                                     facecolor=color)
        ax.add_patch(box)
        ax.text(x + width / 2, y + height / 2, text, ha='center', va='center',
                fontsize=10, wrap=True)

    def add_arrow(x1, y1, x2, y2):
        ax.annotate('', xy=(x2 + 1.9, y2 + 1.2), xytext=(x1 + 1.9, y1),
                    arrowprops=dict(arrowstyle='->', lw=1.5))

    # Lokalno -> GitHub
    left_x = 0
    left_y_positions = [9, 7.5, 6, 4.5, 3]
    left_texts = [
        "git checkout main",
        "git pull",
        "git checkout -b add-skills-section",
        "git add .\ngit commit -m \"Dodaje sekciju za veštine\"",
        "git push -u origin add-skills-section"
    ]

    for i, (y, text) in enumerate(zip(left_y_positions, left_texts)):
        add_box(left_x, y, text)
        if i < len(left_y_positions) - 1:
            add_arrow(left_x, y, left_x, left_y_positions[i + 1])

    ax.text(left_x + 1.9, 10.5, "1. Lokalno → GitHub", fontsize=12, fontweight='bold', ha='center')

    # GitHub -> Lokalno
    right_x = 7
    right_y_positions = [9, 7.5, 6, 4.5, 3]
    right_texts = [
        "Na GitHub-u:\nKreiraj granu 'add-skills-section'",
        "git fetch",
        "git checkout add-skills-section",
        "git add .\ngit commit -m \"Dodaje sekciju za veštine\"",
        "git push"
    ]

    for i, (y, text) in enumerate(zip(right_y_positions, right_texts)):
        add_box(right_x, y, text)
        if i < len(right_y_positions) - 1:
            add_arrow(right_x, y, right_x, right_y_positions[i + 1])

    ax.text(right_x + 1.9, 10.5, "2. GitHub → lokalno", fontsize=12, fontweight='bold', ha='center')

    # Sačuvaj sliku i/ili prikaži
    plt.savefig("dijagram.png", dpi=300)
    plt.show()

draw_diagram()
