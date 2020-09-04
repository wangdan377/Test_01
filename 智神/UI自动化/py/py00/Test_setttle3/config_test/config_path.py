import configparser
import os

#获取配置文件路径
conf_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'config_test', 'api_test.ini') #取四层路径下的文件
print(conf_path)
#读取配置文件
conf = configparser.ConfigParser()
conf.read(conf_path, encoding="utf8")
js_url = conf.get("JS_URL", "js_url")
app_id = conf.get('APP_ID','app_id')
