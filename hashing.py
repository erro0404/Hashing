# This is case-sensitive as it utilizes ASCII-values of letters to return an int-value of the letters.
# USE UPPER-CASE
def alphabet_converter(letters = []):
    for i in range(len(letters)):
        letters[i] = (ord(letters[i]) - 64)
    return letters

def number_converter(numbers = []):
    for i in range(len(numbers)):
        numbers[i] = chr(numbers[i] + 64)
    return numbers

# Returns a hash_value given from modulus operation of letter % mod_value.
def hash1(letter_value, mod_value):
    return (letter_value % mod_value)

# Returns a hash_value given from a constant 'hash_value' sent as a parameter.
# This sentralizes the values close to eachother, giving better efficiency than hash1.
def hash2(letter_value, hash_value):
    return (hash_value - (letter_value % hash_value))

# Linear Probing utilizes indexations with itself += 1.
# Double Hashing utilizes indexations with itself += additional.
# Both methods returns the index based on the modulus operation index %= mod_value.
# Double Hashing collides less than Linear Probing, and therefore is more efficient.
def insert(new_array, hash_type, letter_value, hash_value, mod_value):
    index = hash1(letter_value, mod_value)
    additional = hash2(letter_value, hash_value)
    
    # Finds an empty space in the array.
    while (new_array[index] != -19):
        if (hash_type == "LinearProbing"):
            #print("lp")
            index += 1
        else:
            #print("dh")
            index += additional
        index %= mod_value
        
    new_array[index] = letter_value
