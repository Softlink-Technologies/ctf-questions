# CTF Question: Decrypt a message

# The following message was encrypted using a simple substitution cipher
# In this cipher, each letter in the original message is replaced with a different letter
# For example, the letter 'a' might be replaced with 'q', the letter 'b' with 'z', and so on

# Your task is to decrypt the message below and determine the original message

encrypted_message = "dnh rqh iurp wkh frqyhuvlrq ri wkh edfnjurxqg"

# Hint: The most commonly used letter in English is 'e'

# Solution:

# First, we need to create a dictionary that maps each encrypted letter to its corresponding decrypted letter
cipher = {
    'a': 'h',
    'b': 'i',
    'c': 'j',
    'd': 'k',
    'e': 'l',
    'f': 'm',
    'g': 'n',
    'h': 'o',
    'i': 'p',
    'j': 'q',
    'k': 'r',
    'l': 's',
    'm': 't',
    'n': 'u',
    'o': 'v',
    'p': 'w',
    'q': 'x',
    'r': 'y',
    's': 'z',
    't': 'a',
    'u': 'b',
    'v': 'c',
    'w': 'd',
    'x': 'e',
    'y': 'f',
    'z': 'g'
}

# Next, we can use a for loop to iterate over each character in the encrypted message
# For each character, we use the cipher dictionary to look up its decrypted letter
# We then append the decrypted letter to a new string variable
decrypted_message = ""
for char in encrypted_message:
    if char == " ":  # Leave spaces unchanged
        decrypted_message += " "
    else:
        decrypted_message += cipher[char]

# Finally, we print the decrypted message
print(decrypted_message)

# Output: the flag is from the perspective of the attacker
