import instaloader

bot = instaloader.Instaloader()
profile = instaloader.Profile.from_username(bot.context, 'bugatti')

print(type(profile))

print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Follow list: ", profile.followees)
print("Bio: ", profile.biography, profile.external_url)

bot.login(user="theone__aladin", passwd="Aladin1151")

bot.interactive_login("your username")

profile.followers = [profile.followers.username for follower in profile.get_followers()]
profile.followees = [followee.username for followee in profile.get_followees()]
print(profile.followers)

profile = instaloader.Profile.from_username(bot.context, 'bugatti')
posts = profile.get_posts()
for index, post in enumerate(posts, 1):
    bot.download_post(post, target="{profile.username}_{index}")