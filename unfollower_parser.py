import json

f = open("followers_1.json","r")
followers_raw = json.loads(f.read())
followers_list = []

follower_count = 0
for each_follower in followers_raw:
	name = each_follower.get('string_list_data')[0].get('value')
	follower_count +=1
	followers_list.append(name)

f = open("following.json","r")
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