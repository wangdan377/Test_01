'''
@Author: xiaomin
@Date: 2020-04-29 16:57:51
@LastEditTime: 2020-05-11 11:15:25
@LastEditors: xiaomin
@Description: 用户的设备设置属性和期望属性值流程
@FilePath: \ioT-uat\Testcase\test15_userdevice03.py
'''

import os
import sys
sys.path.append("..")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import unittest
import requests
import json
import ddt
import time

from Params.params import userDeviceTest03
from Common.test_init_data import initData
from Common.casefunction import CaseFunction
from Common.Requestsfun import requestMethod
from Common.comm import loginToken
from Common.config import Config


@ddt.ddt
class userDeviceTest_03(loginToken):
    '''
    创建产品-创建设备-绑定设备-定义优模型属性-发布产品-设置属性-查询属性-批量设置属性-查询属性-设置期望属性值-查询期望属性值
    '''
    @ddt.data({'title':'直连产品','dataFormat':'1','networkType':'WIFI','productName':'apitest_auto40','productNodeType':'0','sub':'false'},
              {'title':'网关子设备产品','dataFormat':'0','networkType':'WIFI','productName':'apitest_auto41','productNodeType':'0','sub':'true'},
              {'title':'边缘网关产品','dataFormat':'1','networkType':'WIFI','productName':'apitest_auto42','productNodeType':'2','sub':'false'})
    @ddt.unpack
    def test_userdevice_03(self,dataFormat,networkType,productName,productNodeType,sub,title):

        # '''数据初始化'''
        a=initData()
        a.initdata({'productName':productName})

        # 变量用来控制调取接口索引
        i=0

        '''获取test_userdevice3.yaml中的数据'''
        data=userDeviceTest03()
        request=requestMethod()
        urls=data.url
        headers=data.header
        para=data.data
        expcode=data.code

        '''给所有url补充域名'''
        url=[None]*len(urls)
        for n in range(0,len(urls)):
            if 'oauth/login' not in urls[n] and 'utmodel' not in urls[n]:
                url[n]=Config.host+urls[n]
            else:
                url[n]=urls[n]

        '''登录用户'''
        print('\n'+url[i])
        print('------登录用户入参------')
        print(para[i])
        response=request.get_post(url[i],headers[i],para[i])
        res_usrtoken=json.loads(response.text)
        curcode=response.status_code
        print('------登录用户返回------')
        print('status:%s'%str(curcode))
        print(str(response.text))
        
        self.assertEqual(expcode[i],curcode)
        i=i+1
        

        '''给接口添加token'''
        for n in range(1,len(headers)):
            if 'deviceOwner' not in urls[n]:
                #开发者接口
                headers[n].update(Authorization='bearer '+loginToken().token)
            else:
                #用户接口
                headers[n].update(Authorization=res_usrtoken['token_type']+' '+res_usrtoken['access_token'])
            
        '''实例化调用测试数据的类'''
        case_function=CaseFunction()  

        '''创建产品'''
        print('\n'+url[i])
        print('------创建产品入参------')
        createproduct=case_function.post_request(request,url[i],headers[i],para[i],{'dataFormat':dataFormat,'networkType':networkType,'productNodeType':productNodeType,'productName':productName,'sub':sub})
        curcode=createproduct.status_code
        print('------创建产品返回------')
        print('status:%s'%str(curcode))
        print(createproduct.text)
        self.assertEqual(expcode[i],curcode)
        createproduct=json.loads(createproduct.text)
        productkeys=createproduct['productKey']
        print('获取产品Key：'+productkeys)
        i=i+1

        '''创建设备'''
        print('\n'+url[i])
        print('------创建设备入参------')
        createdevice=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=createdevice.status_code
        print('------创建设备返回------')
        print('status:%s'%str(curcode))
        print(createdevice.text)        
        self.assertEqual(expcode[i],curcode)
        deviceinfo=json.loads(createdevice.text)
        devicesecret=deviceinfo['deviceSecret']
        i=i+1  

        '''绑定用户'''
        print('\n'+url[i])
        print('------绑定用户入参------')
        binduser=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys,'deviceSecret':devicesecret})
        curcode=binduser.status_code
        print('------绑定用户返回------')
        print('status:%s'%str(curcode))
        print(str(binduser.text))
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''查询产品虚拟子产品key'''
        print('\n'+url[i])
        getproduct=case_function.get_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=getproduct.status_code
        print('------查询产品虚拟子产品key返回------')   
        print('status:%s'%str(curcode))
        print(getproduct.text)
        gmtmodel_res=json.loads(getproduct.text)
        gmtmodelid=gmtmodel_res["subProductKey"]
        i=i+1

        '''查询产品优模型id'''
        if para[1]['productName']=='apitest_auto42':
            para[i]['identifier']=gmtmodelid
        else:
            para[i]['identifier']=productkeys
        print('\n'+url[i])
        getmodel=case_function.get_request(request,url[i],headers[i],para[i])
        curcode=getmodel.status_code
        print('------查询产品优模型id返回------')
        print('status:%s'%str(curcode))
        print(getmodel.text)        
        self.assertIn(expcode[i],getmodel.text)
        model_res=json.loads(getmodel.text)
        modelid=model_res["id"]
        i=i+1       

        '''定义属性'''
        print('\n'+url[i])
        print('------定义属性入参------')
        definedserver=case_function.post_request(request,url[i],headers[i],para[i],{'modelId':modelid})
        curcode=definedserver.status_code
        print('------定义属性返回------')
        print('status:%s'%str(curcode))
        print(definedserver.text)        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''发布产品'''
        print('\n'+url[i])
        print('------发布产品入参------')
        releaseproduct=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=releaseproduct.status_code
        print('------发布产品返回------')
        print('status:%s'%str(curcode))
        print(str(releaseproduct.text))        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        time.sleep(2)

        '''设置属性'''
        print('\n'+url[i])
        print('------设置属性入参------')
        setserver=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=setserver.status_code
        print('------设置属性返回------')
        print('status:%s'%str(curcode))
        print(str(setserver.text))        
        self.assertEqual(expcode[i],curcode)
        i=i+1

        '''查询属性'''
        print('\n'+url[i])
        getserver=case_function.get_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=getserver.status_code
        print('------查询属性返回------')   
        print('status:%s'%str(curcode))
        print(getserver.text)
        self.assertNotIn(expcode[i],getserver.text)
        i=i+1
        
        '''批量设置属性'''
        print('\n'+url[i])
        print('------批量设置属性入参------')
        setservers=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=setservers.status_code
        print('------批量设置属性返回------')
        print('status:%s'%str(curcode))
        print(str(setservers.text))        
        self.assertEqual(expcode[i],curcode)
        i=i+1      

        '''查询属性'''
        print('\n'+url[i])
        getserver=case_function.get_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=getserver.status_code
        print('------查询属性返回------')   
        print('status:%s'%str(curcode))
        print(getserver.text)
        self.assertNotIn(expcode[i],getserver.text)
        i=i+1

        '''设置期望属性值'''
        print('\n'+url[i])
        print('------设置期望属性值入参------')
        setdesire=case_function.post_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=setdesire.status_code
        print('------设置期望属性值返回------')
        print('status:%s'%str(curcode))
        print(str(setdesire.text))        
        self.assertEqual(expcode[i],curcode)
        i=i+1
        
        '''查询期望属性值'''
        print('\n'+url[i])
        getdesire=case_function.get_request(request,url[i],headers[i],para[i],{'productKey':productkeys})
        curcode=getdesire.status_code
        print('------查询期望属性值返回------')   
        print('status:%s'%str(curcode))
        print(getdesire.text)
        self.assertIn(expcode[i],getdesire.text)
        
        '''数据清理'''
        a.initdata({'productName':productName})


if __name__ == '__main__':
    unittest.main(verbosity=2)
