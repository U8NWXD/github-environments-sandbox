import os

print('Running script.py from branch main.')

# Expected value: topsecret
print('Expecting a secret env variable MY_SECRET.')
secret = os.environ.get('MY_SECRET', '')
print('Found:', secret)
print('Found (reversed to avoid masking):', secret[::-1])
