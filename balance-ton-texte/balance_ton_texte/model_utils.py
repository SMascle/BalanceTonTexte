# Model ML : 
	# sudo docker run -it -p 5000:5000 quay.io/codait/max-text-summarizer

import requests

def summarize(text): 

	print(text)

	debug = False

	url = 'http://127.0.0.1:5001/model/predict'

	data = {'text': [text]}

	response = requests.post(url, json = data)

	if debug:

		if response.status_code == 200:
			print('Success')
		elif response.status_code == 300:
			print('Redirected')
		elif response.status_code == 400:
			print('Client Error')
		elif response.status_code == 500:
			print('Server Error')
		elif response.status_code == 404:
			print("Page not found")
	import pdb; pdb.set_trace
	return response.json()['summary_text'][0] 

	
if __name__	== '__main__':

	user_text = 'HELLO' 

	resumer =  summarize(user_text)
	
	print(resumer)


