# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of condidates.
# 3. The percentage of votes each candidates who received votes.
# 4. The total number of votes each condidates won.
# 5. The winner of the election based on popular vote.


# Import CSV module
import csv
dir(csv)

# 1. Initialized the total vote counter
total_vote = 0

# Condidate options and condidate votes
condidate_options = []
condidate_votes = {}

# Winning condidate and winning count tracker
winning_condidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
file_to_load = "c:\\Users\\rghaf\Desktop\\UT Data BootCamp\\Working Repo\\03-Election-Analysis\\Resources\\election_results.csv"
with open(file_to_load) as election_data:
   
   # To Do: read and analyze the data here

   file_reader = csv.reader(election_data)
   
   # print the headers row
   headers = next(file_reader)
   #print(headers)

   # counting total vote
   for row in file_reader:
      # 2. Add to the total vote count
      total_vote += 1

      condidate_name = row[2]
      if condidate_name not in condidate_options:

         # Add condidate name to the condidate list
         condidate_options.append(condidate_name)

         # Start tracking condidate's votes
         condidate_votes[condidate_name] = 0

      condidate_votes[condidate_name] += 1


# Open the analysis file to write election results analysis in it
file_to_save = "c:\\Users\\rghaf\Desktop\\UT Data BootCamp\\Working Repo\\03-Election-Analysis\\Analysis\\election_analysis.txt"
with open(file_to_save, "w") as txt_file:

   election_results = (
      f"\nElection Results\n"
      f"---------------------------------\n"
      f"Total Votes: {total_vote:,}\n"
      f"---------------------------------\n")

   print(election_results, end="")
   txt_file.write(election_results)

   for condidate_name in condidate_votes:

      # To print each condidate's name, vote count and percentage of votes to the terminal
      votes = condidate_votes[condidate_name]
      vote_percentage = float(votes) / float(total_vote) * 100
      condidate_result = (f"{condidate_name}: received {vote_percentage:.1f}% ({(votes):,})\n")
      txt_file.write(condidate_result)
      

      # Determine Winning condidate
      if (votes > winning_count) and (vote_percentage > winning_percentage):
         winning_count = votes
         winning_percentage = vote_percentage
         winning_condidate = condidate_name


   winning_condidate_summary = (
      f"--------------------------------\n"
      f"Winner:  {winning_condidate}\n"
      f"Winning Vote Count:  {winning_count:,}\n"
      f"Winning Percentage:  {winning_percentage:.1f}\n"
      f"--------------------------------")

   txt_file.write(winning_condidate_summary)


   
   # 3. Print the total votes.
   #print(total_vote)
   #print(condidate_votes)




#import os
#file_to_load = os.path.join("Resources", "election_results.csv")
#with open(file_to_load) as election_data:
 #   print(election_data)