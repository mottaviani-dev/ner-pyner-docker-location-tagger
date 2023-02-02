import csv
import os
import ner
import sys
import json

def locations_tag(directory):
    locations = {}
    tagger = ner.SocketNER(host='ner_server', port=8888)
    
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r') as f:
                text = f.read()
                entities = tagger.get_entities(text)
                if 'LOCATION' in entities:
                    locations[filename] = entities['LOCATION']
    return locations

def main():
    #Create a json file storing locations dictionary for each
    #directory argument of the script
    directory = 'locations'
   
    locations = locations_tag(directory)

    with open(directory + '.json', 'w') as f:
        f.write(json.dumps(
            locations,
            indent=4,
            separators=(',', ': ')
            )
        )

if __name__ == "__main__":
    main()