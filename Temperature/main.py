temperature = int(input())
humidity = int(input())

if temperature >= 30 and humidity >= 90:
    print("Hot and Humid")
elif temperature >= 30 and humidity < 90:
    print("Hot")
elif temperature < 30 and humidity >= 90:
    print("Cool and Humid")
else:
    print("Cool")