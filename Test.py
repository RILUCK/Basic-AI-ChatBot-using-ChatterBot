import re

pattern = 'do you remember (.*)'

message = 'do you remember when you ate the strawberries in the garden'

pharse = pattern.search(pattern,message).group(1)

print(pharse)