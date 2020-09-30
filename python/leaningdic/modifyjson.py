import os
from os.path import join as pjoin
import json

name_emb = {'e': '5555', 'f': '6666'}

output_dir = '../dataconfig/modifyrequestdata.json'

listdir = os.listdir(output_dir)
if 'emb_json.json' in listdir:
    fr = open(pjoin(output_dir, 'emb_json.json'), 'w')
    model = json.dumps(name_emb)
    fr.write(model)
