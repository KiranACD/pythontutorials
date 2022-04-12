# Main.py

print(f'---------------------------- Running {__name__} -----------------------------\n\n')

import module1
print('Importing module1 again. Nothing should show up as it is already in cache.')
import module1

print(f'\n\n---------------------------- End of {__name__} ------------------------------')

