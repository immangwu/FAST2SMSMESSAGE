import requests
url = "https://www.fast2sms.com/dev/bulkV2"

querystring = { "authorization":"FhRx5XmMvGyW37q0SKbsrkcICu8felZgBaiwU61JoPQ42jHNEDqVtZJza2Cb4fPhLWFe3cDpuliENYOK",
                'sender_id': 'TXTIND',
                'message': 'JESUS LOVES ME',
                'language': 'english',
                'route': 'v3',
                'numbers': '9677817992'	}
headers = {
	
	'Cache-Control': "no-cache"
}

response = requests.request("GET",url,headers = headers, params= querystring)
print(response.text)
