import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.generator import password_generator

pw = password_generator(12)
# pw_short = password_generator(7)
# pw_long = password_generator(65)

print(pw)