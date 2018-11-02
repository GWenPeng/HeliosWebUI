import requests
from  api.Expense_Report_Type import Expense_Report_Type
from api.Get_Oauth_Token_Api import GetOauthTokenApi
class Get_Enble_Expense_FormLists_Api:
    def __init__(self,access_token="05a1d542-e5d9-4c59-955d-7e43aedbcf22",host='https://console.huilianyi.com'):
        #api初始化方法access_token，host为初始化参数
                self.url = host+"/api/custom/forms/my/available"
                self.querystring = {"formType":"102","roleType":"TENANT"}
                self.headers = {
            'Authorization': "Bearer"+access_token,
            'cache-control': "no-cache",
            'Postman-Token': "082b1194-d7b4-4d6c-9b1c-553777e39eab"
            }

    def get_expense_claim_name(self,num,reportType):
        #获取报销单的名称 return第num&reportType类型的报销单名称
        #index 实际为报销单的索引
            response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
            json_response=response.json()
            json_arraylength=len(json_response)
            dictionaries=dict()
            # print(json_response)
            # print(reportType)

            # formType"3003" in json_response[x]

            for index in range(1,json_arraylength+1):
                # print(index)
                if reportType==json_response[index-1]['formType']:
                      dictionaries[index]=json_response[index-1]["formName"]

            return list(dictionaries.values())[num]










if __name__ == '__main__':
    access_token = GetOauthTokenApi(username="19902132186", password="a11111").get_access_token()
    name=Get_Enble_Expense_FormLists_Api(access_token=access_token).get_expense_claim_name(num=1,reportType=Expense_Report_Type.daily_report_type.value)

    print(name)
