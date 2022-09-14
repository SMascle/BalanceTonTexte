# Model ML : 
	# sudo docker run -it -p 5000:5000 quay.io/codait/max-text-summarizer

import requests

def summarize(text): 

	print(text)

	debug = False

	url = 'http://127.0.0.1:5000/model/predict'

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

	return response.json()['summary_text'][0] 

	
if __name__	== '__main__':

	user_text = 'The Korean Air executive who kicked up a fuss over a bag of nuts will resign from her remaining posts with the airline , the company chairman -- who is also her father -- said Friday . The executive , Heather Cho , found herself at the center of a media storm after she ordered that a plane turn back to the gate and that a flight attendant be removed -- all because she was served nuts in a bag instead of on a plate in first class . Although her role put her in charge of in-flight service , she was only a passenger on the flight and was not flying in an official'

	resumer =  summarize(user_text)
	
	print(resumer)


