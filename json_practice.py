
import json


# Convert Json to Python
jsonStr = '{"name": "Aasim", "hobby": "Reading", "color": null}'
pythonDict = json.loads(jsonStr)
print(pythonDict)


# Convert Python to Json
mapping = {
    "name": "Aasim",
    "Profession": "Engineer",
    "Hobbies": "Reading",
    "Lifestyle": None
}

jsonData = json.dumps(mapping, indent=4)
print(jsonData)