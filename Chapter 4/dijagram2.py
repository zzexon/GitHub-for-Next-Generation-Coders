import json
import matplotlib.pyplot as plt

# Učitaj JSON fajl
with open('trends.json', 'r') as f:
    trends = json.load(f)

labels = trends['data']['labels']  # godine
datasets = trends['data']['datasets']  # svi framework-ovi

# Crtanje grafikona
plt.figure(figsize=(10, 6))

for dataset in datasets:
    plt.plot(labels, dataset['data'], label=dataset['label'], color=dataset['borderColor'])

# Naslovi i legende
plt.title(trends['options']['plugins']['title']['text'])
plt.xlabel(trends['options']['scales']['x']['title']['text'])
plt.ylabel(trends['options']['scales']['y']['title']['text'])
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
