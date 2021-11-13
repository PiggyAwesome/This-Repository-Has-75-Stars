"""
Here is the genius program behind this repository
"""


import requests
import time
import random
from github import Github


token = ""

gh = Github(token)

headers = {"Accept": "application/vnd.github.v3+json", "Authorization": f"token {token}"}

while True:
    repos = requests.get("https://api.github.com/users/PiggyAwesome/repos?per_page=100", headers=headers)
    for thingy in repos.json():
        if "this-repository-has" in thingy["name"].lower():
            name = thingy["name"]
            print(name, thingy["stargazers_count"])
            if f"This-Repository-Has-{thingy['stargazers_count']}-Stars" != name:
                sha = requests.get(f"https://api.github.com/repos/PiggyAwesome/{name}/contents/README.md").json()["sha"]
                commitMessages = [f"Pretty sure i wrote {thingy['stargazers_count']}", f"omg another mistake? I'm sure i wrote  {thingy['stargazers_count']} last time!", f"Spelling mistake!", f"This repo is weird. Im sure i typed {thingy['stargazers_count']} last time!"]
                repo = gh.search_repositories(name)[0]
                repo.update_file("README.md", random.choice(commitMessages), f"# I bet you can't prove me wrong!\n\n{thingy['stargazers_count']} Stars!", sha=sha)
                repo.edit(name=f"This-Repository-Has-{thingy['stargazers_count']}-Stars")
                print("Updated!")
            break
    time.sleep(500)


            
