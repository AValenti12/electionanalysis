
#print("Hello World!")

#counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
 #   print(counties[1])

 #3.2.5 create list
counties = ["Arapahoe","Denver","Jefferson"]
#print(counties)
#print(counties[0])
#print(counties[2])
#print(counties[-1])
#print(counties[-2])
#print(len(counties))
#slice lists list[start:end]
#print(counties[0:2])
#print(counties[0:1])
#print(counties[0:1])
#print(counties[:2])
#print(counties[1:])
#counties.append("El Paso")
#print(counties)
#counties.insert(2, "El Paso")
#print(counties)
#counties.remove("El Paso")
#print(counties)
#counties.pop(3)
#print(counties)
#counties[2]="El Paso"
#print(counties)

#3.2.6 Data Structures: Tuples
#my_tuple=()
#counties_tuple=("Arapahoe","Denver","Jefferson")
#print(len(counties_tuple))
#print(counties_tuple[1])

#3.2.7 Dictionaries
#my_dictionary = {}
counties_dict={}
counties_dict["Arapahoe"] = 422829
#print(counties_dict)
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
#print(counties_dict)
#print(len(counties_dict))
#print(counties_dict.items())
#print(counties_dict.keys())
#print(counties_dict.values())
#print(counties_dict.get("Denver"))
#print(counties_dict[Arapahoe])
#print(counties_dict['Arapahoe'])
#Lists of Dictionaries
#voting_data = []
#voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
#voting_data.append({"county":"Denver", "registered_voters": 463353})
#voting_data.append({"county":"Jefferson", "registered_voters": 432438})
#print(voting_data)

#3.2.8 Decision Statements
# How many votes did you get?
#my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
#total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")

#counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
 #   print(counties[1])

#counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
 #   print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not the list of counties.")
#if "Arapahoe" in counties and "El Paso" in counties:
#    print("Arapahoe and El Paso are in the list of counties.")
#else:
#    print("Arapahoe or El Paso is not in the list of counties.")


#3.2.9 Membershiop and logical operations
#counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not the list of counties.")
#if "Arapahoe" in counties and "El Paso" in counties:
#    print("Arapahoe and El Paso are in the list of counties.")
#else:
#    print("Arapahoe or El Paso is not in the list of counties.")
#if "Arapahoe" in counties or "El Paso" in counties:
#    print("Arapahoe or El Paso is in the list of counties.")
#else:
#    print("Arapahoe and El Paso are not in the list of counties.")

#3.2.10 Repetition statments
#x = 0
#while x <= 5:
#    print(x)
#    x = x + 1
#for county in counties:
#    print(county)
#numbers = [0, 1, 2, 3, 4]
#for num in numbers:
#    print(num)
#simplified code
#for num in range(5):
#    print(num)
#for i in range(len(counties)):
#    print(counties[i])
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#to get keys from dictionary
#for county in counties_dict:
#    print(county)
#for county in counties_dict.keys():
#    print(county)
#to get values of dictionary
#for voters in counties_dict.values():
#    print(voters)
#for counties list
#for county in counties_dict:
#    print(counties_dict[county])
#for county, voters in counties_dict.items():
#    print(county, voters)
#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                {"county":"Denver", "registered_voters": 463353},
#                {"county":"Jefferson", "registered_voters": 432438}]
#
#for county_dict in voting_data:
#    print(county_dict)
#for county_dict in voting_data:
#    print(county_dict['county'])
#skill drill
#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#for county, voters in counties_dict.items():
#    print(county + " county has " + str(voters) + " registered voters.")

#3.2.11 printing formats
#edited code
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")
#edited code
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")
# Edited code again
#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
#    f"You received {candidate_votes} number of votes. "
#    f"The total number of votes in the election was {total_votes}. "
#    f"You received {candidate_votes / total_votes * 100}% of the total votes.")
#print(message_to_candidate)
#FORMAT FLOATIND POINT DECIMAL
#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
#    f"You received {candidate_votes} number of votes. "
#    f"The total number of votes in the election was {total_votes:,}. "
#    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
#print(message_to_candidate)
#skill Drill
#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#for county, voters in counties_dict.items():
#    print(county + " county has " + str(voters) + " registered voters.")