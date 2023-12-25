import json
import argparse

parser = argparse.ArgumentParser(description="Getting filenames")

parser.add_argument("--followerfile", '-ff', default="followers.json", help="Filename of followers datafile (including the .json)")
parser.add_argument("--followingfile", '-fi', default="following.json", help="Filename of following datafile (including the .json)")

args = parser.parse_args()

try:
	f = open(args.followerfile,"r")
except Exception as e:
	print(e)
	print("\n ------------------------------------------------------ \n\
Did you forget to upload the follower filename? Type \'python unfollower_parser.py --help\' for more information. \
\n ------------------------------------------------------ \n")

followers_raw = json.loads(f.read())
followers_list = []

follower_count = 0
for each_follower in followers_raw:
	name = each_follower.get('string_list_data')[0].get('value')
	follower_count +=1
	followers_list.append(name)

try:
	f = open(args.followingfile,"r")
except Exception as e:
	print(e)
	print("\n ------------------------------------------------------ \n\
Did you forget to upload the following filename? Type \'python unfollower_parser.py --help\' for more information. \
\n ------------------------------------------------------ \n")


following_raw = json.loads(f.read())
following_list = []

following_count = 0
for each_following in following_raw.get('relationships_following'):
	name = each_following.get('string_list_data')[0].get('value')
	following_count += 1
	following_list.append(name)

counter = 0
for each_following in following_list:
	if each_following not in followers_list:
		print(each_following)
		counter += 1

print('------------------------------------------------------')
print(counter, "people do not follow you back right now.")
print("following: ", following_count)
print("followers: ", follower_count)