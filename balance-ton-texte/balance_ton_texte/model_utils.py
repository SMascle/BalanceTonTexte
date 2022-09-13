import requests

url = 'http://127.0.0.1:5000/model/predict'

data = {'text': value}

x = requests.post(url, json = data)

if x.status_code == 200:

	print('Success')
	
elif x.status_code == 404:

	print("Page not found")
    
for k, v in x.json().items():

	print(k, ": ", v)
 
	
    
    
#print("Status Code", x.status_code)

#print("content of request ", x.json())

#print(x, x.text)



