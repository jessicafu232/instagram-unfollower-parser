# Instagram Unfollower Parser!
A program that can detect the account usernames of individuals who are not following the user back, by using the follower and following data files from the Instagram data download.

# Usage
No login required. All that's needed is to download the data files given by Instagram's data download feature. Select the "Followers and following" download option when requesting to download specific files. To run the program, take the "followers" and "following" files and move them into the same folder as the unfollower_parser.py file. 
# IMPORTANT: Ensure that the data download is in JSON format, and the date range is "All time". 

# Running
Python needs to be installed into the machine for the program to run. 
To run the program, type 'python unfollower_parser.py'. If the filenames of your follower/following files are NOT 'followers.json' and 'following.json', you need to use the run arguments of '-ff' and '-fi'. 

The argument descriptions are as follows:

`--followerfile`, `-ff`
* Filename of followers datafile (including the .json) (i.e. `follower_1.json`)

`--followingfile`, `-fi`
* Filename of following datafile (including the .json) (i.e. `following_1.json`)

Running the program should print out the number of people not following back, and their usernames. Happy hunting!
