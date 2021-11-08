countries = {"Iran" : 422 , "USA" : 356 , "UAE" : 123, "Japan" : 512, "France" : 431, "Italy" : 521, "Germany" : 425, "Iraq" : 842}
for country, votes in countries.items():
    print(f"{country} country has {votes} registered votes.")


voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for county_dic in voting_data :
    print(f"{county_dic['county']} county has {county_dic['registered_voters']} registered voters.")