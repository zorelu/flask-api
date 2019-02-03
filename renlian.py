##这个人脸识别的demo
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.iai.v20180301 import iai_client, models
import json
try:
    cred = credential.Credential("AKIDeBWfdSkh2EE3gMzDMNDrKUTHwY3TjngO", "TmvypUxEJCzf9RWP5QegWDkBQUN4d4MU")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "iai.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = iai_client.IaiClient(cred, "ap-guangzhou", clientProfile)
    req = models.VerifyFaceRequest()
    ###获取图片转换格式
    img='{"Url":"http://www.gzywwl.com/4.png","PersonId":"001"}'
    data =json.loads(img)
    data['Url'] ="http://www.gzywwl.com/1.jpg"
    getdata = json.dumps(data)
    params = str(getdata)
    req.from_json_string(params)

    resp = client.VerifyFace(req)
    data=resp.to_json_string()
    ##输出为dict/json并判断
    bllon=json.loads(data)
    print(bllon)
    print(bllon['IsMatch'])
except TencentCloudSDKException as err:
    print(err)
