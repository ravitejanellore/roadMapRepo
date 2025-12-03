import json
def whereContains(id,list,attr):
    for index in range(0,len(list)):
        if list[index][str(attr)]==id:
            return index
        else:
            continue
def readJson(file_name):
    try:
        # 1. Open the file in read mode ('r')
        # 'with open(...)' ensures the file is closed automatically
        with open(file_name, 'r') as file:      
            # 2. Use json.load() to read the data from the file object.
            # This converts the JSON text into a Python object (e.g., dict or list).
            data = json.load(file)
        print("✅ File reading successful. Imported Python Object:")
        print(f"Data type: {type(data)}")
        return data
    # Use pprint for clean dictionary/list output
        pprint.pprint(data)
    except FileNotFoundError:
        print(f"❌ Error: The file '{file_name}' was not found.")
    except json.JSONDecodeError:
        print("❌ Error: The file content is not valid JSON format.")
def writeJson(file_name,tasks):
    # 'w' mode opens the file for writing. If it doesn't exist, it creates it.
    with open(file_name, 'w') as json_file:
    # json.dump(data, file_object, indent=4)
    # The 'indent=4' makes the JSON file human-readable
        json.dump(tasks, json_file, indent=4) 

def getTextinsideQuotes(str,start_delimiter,end_delimiter):
    firstQuoteIndex=int(str.index(start_delimiter))
    secondQuoteIndex=int(str.index(end_delimiter,firstQuoteIndex+1))
    return str[firstQuoteIndex+1:secondQuoteIndex]