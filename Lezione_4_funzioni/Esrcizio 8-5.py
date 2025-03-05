#Esrcizio 8-5
def describe_city (city:str, country:str = "Italy"):
    print(f"{city} is in {country}")

describe_city("Torino")
describe_city("Firenze")
describe_city("New York", "USA")

