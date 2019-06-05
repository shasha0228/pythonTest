import subprocess
import json

print("Board ID: ")
board_id = raw_input()
print("AD ID: ")
_id = raw_input()
print("Password: ")
_pw = raw_input()
cmd = ['curl', '-X', 'POST', '-u', _id+':'+_pw, 'http://sas.lge.com/api/board/bl/'+board_id]
p=subprocess.Popen(cmd, shell=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
origin_data = p.communicate()[0] 

sas_data = json.loads(origin_data)
print(sas_data['boardInfo']['basicInfo']['branch'])
print(sas_data['boardInfo']['basicInfo']['sourceManifest'])
