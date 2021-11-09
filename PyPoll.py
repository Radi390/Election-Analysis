# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of condidates.
# 3. The percentage of votes each candidates who received votes.
# 4. The total number of votes each condidates won.
# 5. The winner of the election based on popular vote.


# Import CSV module
import csv
dir(csv)

# Open the election results and read the file.
file_to_load = "c:\\Users\\rghaf\Desktop\\UT Data BootCamp\\Working Repo\\03-Election-Analysis\\Resources\\election_results.csv"
with open(file_to_load) as election_data:
   
   # To Do: read and analyze the data here

   file_reader = csv.reader(election_data)
   
   # print the headers row
   headers = next(file_reader)
   print(headers)
   #for row in file_reader:
    #  print(row[0])

# Open the analysis file to write election results analysis in it
file_to_save = "c:\\Users\\rghaf\Desktop\\UT Data BootCamp\\Working Repo\\03-Election-Analysis\\Analysis\\election_analysis.txt"
with open(file_to_save, "w") as txt_file:
   txt_file.write("Counties in the Election\n--------------------------\n")
   txt_file.write("Arapahoe\nDenver\nJefferson")


#import os
#file_to_load = os.path.join("Resources", "election_results.csv")
#with open(file_to_load) as election_data:
 #   print(election_data)