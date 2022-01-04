counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print("Denver")
if counties[2] != "Jefferson":
    print(counties[2])
if "El Paso" in counties:
    print("El Paso's there")
else:
    print("El Paso isn't there")
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Arapahoe is in the list and El Paso is not")
else:
    print("Arapahoe and/or El Paso aren't on the list")
for county in counties:
    print(county)
for i in range(len(counties)):  
    print(counties[i])
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county, voters in counties_dict.items():
    print(county, " county has ", voters, " registered voters.")
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]    
for county_dict in voting_data:
    print(county_dict)
for i in range(len(voting_data)):
    print(voting_data[i]['county'])
for county_dict in voting_data:
    for key in county_dict.keys():
        print(key)
for county_dict in voting_data:
     for value in county_dict.values():
         print(value)
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for counties_dict in voting_data:
    for county in counties_dict:
        for voters in counties_dict:
            print(f"{county} county has {voters} registered voters.")

