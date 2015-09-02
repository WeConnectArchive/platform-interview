import hashlib
import json
fname = 'data.log'
fh = open('output.log','w')
with open(fname, 'r') as fin:
	for line in fin.read().split('\n'):
		if "INFO" in line or "WARN" in line:
			new_line = line.split(": ")
			json_data = json.loads(new_line[1])
			sn_hashed =  hashlib.md5(json_data['sn']).hexdigest()
			json_data['sn'] = sn_hashed
			new_line[1] = json.dumps(json_data)
			line = ": ".join(new_line) 
		
		print line
		fh.write('\n')	
		fh.write(line)