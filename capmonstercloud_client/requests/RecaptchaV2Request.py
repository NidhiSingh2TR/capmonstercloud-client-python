from typing import Dict, Union
from pydantic import Field
from .RecaptchaV2RequestBase import RecaptchaV2RequestBase
from .proxy_info import ProxyInfo


class RecaptchaV2Request(RecaptchaV2RequestBase, ProxyInfo):
    
    type: str = Field(default="NoCaptchaTask")

    def getTaskDict(self) -> Dict[str, Union[str, int]]:
        task = {}
        task['type'] = self.type
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        task['proxyType'] = self.proxy_type
        task['proxyAddress'] = self.proxy_address
        task['proxyPort'] = self.proxy_port
        task['proxyLogin'] = self.proxy_login
        task['proxyPassword'] = self.proxy_password

        if self.dataSValue is not None:
           task['recaptchaDataSValue'] = self.dataSValue
        
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent

        if self.cookies is not None:
            task['cookies'] = self.cookies

        return task
    