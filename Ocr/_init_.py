from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.ocr.v20181119 import ocr_client, models 
import json
def OcrMethod(Base64,SecretId,SecretKey):
    try: 
        cred = credential.Credential(SecretId, SecretKey) 
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = ocr_client.OcrClient(cred, "ap-guangzhou", clientProfile) 

        req = models.GeneralBasicOCRRequest()
        params = '{\"ImageBase64\":\"+' Base64 '+\"}'
        req.from_json_string(params)

        resp = client.GeneralBasicOCR(req) 
        jsonstr = json.loads(resp.to_json_string())
        array = jsonstr['TextDetections']
        s = ''
        for i in array:
            s = s + i['DetectedText']
        return s
        # f = open('C:\\Users\\hasee\\Documents\\UiPath\\Play\\1.txt','w')
        # f.write(s)
        # return '1'
    except TencentCloudSDKException as err: 
        print(err) 