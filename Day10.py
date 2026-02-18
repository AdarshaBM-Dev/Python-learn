#whlie
is_failed = True
i = 1 #attempt

while is_failed and i <= 100:    # coditio  one
    print(f"Try {i}")
    i = i + 1 
print ("I gave up")

while is_failed:      #condiion two
    print(f"Try {i}")
    i = i + 1
    if i>100:
        break
print ("I gave up")





