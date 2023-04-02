import os
import shutil
import random
random.seed(123456789)

ALL_EMOJIS_ROOT = 'png'
SAMPLED_EMOJIS_ROOT = 'sampled_emojis'

with open('emojis_pool.txt', 'r') as f:
    emojis_pool = f.read().splitlines()

all_valid_emojis = []
for resolution in os.listdir(ALL_EMOJIS_ROOT):
    for image in os.listdir(os.path.join(ALL_EMOJIS_ROOT, resolution)):
        if image in emojis_pool:
            all_valid_emojis.append(os.path.join(resolution, image))


sampled_emojis = random.sample(all_valid_emojis, k=150)
sampled_emojis.sort()

os.makedirs(SAMPLED_EMOJIS_ROOT, exist_ok=True)
for image in sampled_emojis:
    src = os.path.join(ALL_EMOJIS_ROOT, image)
    dst = os.path.join(SAMPLED_EMOJIS_ROOT, image.replace('/', '_'))
    shutil.copy(src, dst)

