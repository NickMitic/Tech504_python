story1 = {"start":"Something","middle":"then something else","end":"then it was done"}
print(story1)
print(type(story1))
print(story1.keys())
print(story1.values())
print(story1["This is how it started."])
print(story1["Then this happened."])
print(story1["It ended up like this."])
story1["character"] = "James"
print(f"The end. I hope you enjoyed this awful story about {story1["character"]}.")
