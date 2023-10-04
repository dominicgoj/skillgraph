import matplotlib.pyplot as plt
import matplotlib.font_manager
import numpy as np

skills = {
    "Python": 0.8,
    "Django/REST": 0.7,
    "React Native/JS": 0.7,
    "AWS": 0.4,
    "HTML": 0.7,
    "CSS": 0.6,
    "PHP": 0.2,
    "Javascript": 0.3,
    "MySQL": 0.3,
}
font_family = "Arial Rounded MT Bold"
font_families = [f.name for f in matplotlib.font_manager.fontManager.ttflist]
max_circles_per_row = 1
cmap = plt.get_cmap("Greens")
num_circles = len(skills)
num_rows = (num_circles + max_circles_per_row - 1)//max_circles_per_row
circles_radius = 0.4
spacing = 0.5
fig, ax = plt.subplots(figsize=(len(skills)*2, 8))
fig_width = max_circles_per_row * (circles_radius + spacing)
fig_height = num_rows * (2 * circles_radius + spacing)

for i, (skill, value) in enumerate(skills.items()):
    row = i // max_circles_per_row
    col = i % max_circles_per_row


    x = col * (2*circles_radius + spacing)
    y = -row * (2 * circles_radius + spacing)
    color = cmap(value)
    circle = plt.Circle((x, y), circles_radius, color=color)
    ax.add_patch(circle)
    ax.text(x+0.6, y-0.15, skill, ha='left', fontfamily=font_family, fontsize=14)


ax.set_xlim(-0.5, 5)
ax.set_ylim(-fig_height+0.5, 0.5)
ax.axis("off")

plt.show()
