import datetime
import os
import requests
import time
import json
def feed(path,post_url):
	for illumina_dir in os.listdir(path):
		data={}
		raw_createdtime = os.path.getctime(os.path.join(path,illumina_dir))
		illumina_date = datetime.datetime.fromtimestamp(raw_createdtime).strftime('%Y-%M-%d')
		
		data["name"] = illumina_dir
		data["date"] = illumina_date
		res=requests.post(post_url,data)
		if not res.ok:
			print "Couldnt create new data"




if __name__ == "__main__":
	f=open("./config.json","r")
	config = json.load(f)
	illumina_path = config['illumina_store']
	post_url = config['api'] + "/illumina/"

	feed(illumina_path,post_url)
