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
file_to_load = 'C:\Users\rghaf\Desktop\UT Data Bootcamp\Working Repo\03-Election-Analysis\Resources\election_results.csv'
with open(file_to_load) as election_data:
    print(election_data)

import os
print(dir(os.path))