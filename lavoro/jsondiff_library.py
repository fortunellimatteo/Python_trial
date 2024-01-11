import jsondiff

obj1 = {
    "countries": [
        {
            "name": "Great Britian",
            "cities": [{"name": "Manchester"}, {"name": "London"}],
        }
    ]
}

obj2 = {
    "countries": [
        {
            "name": "Great Britian",
            "cities": [{"name": "Manchester"}, {"name": "Lonon"}],
        }
    ]
}

res = jsondiff.diff(obj1, obj2)
sim = jsondiff.similarity(obj1, obj2)
patch = jsondiff.patch(obj1, obj2)

if res:
    print("Diff found")
    print(res)
    print(sim)
    print(patch)
else:
    print("Same")
    print(res)
    print(sim)
    print(patch)