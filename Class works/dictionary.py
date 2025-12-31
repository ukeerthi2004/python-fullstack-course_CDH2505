# ============================================
# PYTHON DICTIONARY METHODS – EXAMPLES
# ============================================

# Creating a dictionary
d = {'N1': 'swetha', 'N2': 'keerthi', 'N3': 'Ravali'}

# --------------------------------------------
# pop() – Removes a value using its KEY
# --------------------------------------------

d.pop('N3')              # Removes key 'N3' and returns its value
# Output returned: 'Ravali'
# Dictionary now becomes: {'N1': 'swetha', 'N2': 'keerthi'}

# --------------------------------------------
# popitem() – Removes the LAST inserted item
# --------------------------------------------

d.popitem()              # Removes last key-value pair
# Output returned: ('N2', 'keerthi')
# Dictionary now becomes: {'N1': 'swetha'}

# --------------------------------------------
# del – Deletes a specific key-value pair
# --------------------------------------------

del d['N1']              # Deletes key 'N1'
# Dictionary now becomes: {}

# --------------------------------------------
# Dictionary View Methods
# --------------------------------------------

d = {'N1': 'swetha', 'N2': 'keerthi', 'N3': 'Ravali'}

d.keys()                 # Returns all keys
# Output: dict_keys(['N1', 'N2', 'N3'])

d.values()               # Returns all values
# Output: dict_values(['swetha', 'keerthi', 'Ravali'])

d.items()                # Returns key-value pairs as tuples
# Output: dict_items([('N1', 'swetha'), ('N2', 'keerthi'), ('N3', 'Ravali')])

# --------------------------------------------
# clear() – Removes all items from dictionary
# --------------------------------------------

d.clear()                # Same as making dictionary empty {}
# d becomes {}

# ============================================
# BUILT-IN FUNCTIONS WITH DICTIONARY
# ============================================

# Creating dictionary again
d = {
    'N1': 'swetha',
    'N2': 'keerthi',
    'N3': 'Ravali',
    'N4': 'shushumitha',
    'N5': 'tanmiy'
}

len(d)                   # Returns number of key-value pairs
# Output: 5

max(d)                   # Returns maximum KEY (alphabetical order)
# Output: 'N5'

min(d)                   # Returns minimum KEY
# Output: 'N1'

sorted(d)                # Returns sorted list of KEYS
# Output: ['N1', 'N2', 'N3', 'N4', 'N5']

# ============================================
# END OF FILE
# ============================================
