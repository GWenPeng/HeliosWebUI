import requests
class GetOauthTokenApi:
    def __init__(self,username="13323454321",password='hly123',host='https://console.huilianyi.com'):
        self.url = host+"/oauth/token"
        self.payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n"+username+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n"+password+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"grant_type\"\r\n\r\npassword\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"scope\"\r\n\r\nwrite\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        self.headers = {
                'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
                'Authorization': "Basic QXJ0ZW1pc0FwcDpuTENud2RJaGl6V2J5a0h5dVpNNlRwUURkN0t3SzlJWERLOExHc2E3U09X",
                'cache-control': "no-cache",
                'Postman-Token': "58061079-6985-4677-85ea-ad89531f9ece"
            }
    def get_access_token(self):
        #获取access_token
        response = requests.request("POST", self.url, data=self.payload, headers=self.headers)

        json_response=response.json()

        return json_response["access_token"]

    def get_refresh_token(self):
        # 获取refresh_token
        response = requests.request("POST", self.url, data=self.payload, headers=self.headers)
        jsonresponse = response.json()

        return jsonresponse["refresh_token"]




if __name__ == '__main__':
    access_token=GetOauthTokenApi(username="19902132186",password="a11111").get_access_token()
    print(access_token)