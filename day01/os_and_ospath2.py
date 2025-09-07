import os.path as op 

PATHS = [
'/one/two/three',
'/one/two/three',
'/',
'.',
'',
]

for p in PATHS:
    print(f'{p} : {op.basename(p)}') 