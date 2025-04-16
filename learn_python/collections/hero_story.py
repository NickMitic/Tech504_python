story1 = {"start":"Something","middle":"then something else","end":"then it was done"}
print(story1)
print(type(story1))
print(story1.keys())
print(story1.values())
print(story1["start"])
print(story1["middle"])
print(story1["end"])
story1["character"] = "James"
print(f"The end. I hope you enjoyed this awful story about {story1["character"]}.")
