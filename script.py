import os

print('Running script.py from branch malicious.')

# Expected value: topsecret
print('Expecting a secret env variable MY_SECRET.')
secret = os.environ.get('MY_SECRET', '')
print('Found:', secret)
print('Found (reversed to avoid masking):', secret[::-1])
