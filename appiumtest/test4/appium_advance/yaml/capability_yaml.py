from appium import webdriver
import yaml

file = open('./desired_caps.yaml','r')
data = yaml.load(file,Loader=yaml.FullLoader)
print(data)

desired_caps = {}
desired_caps['platformName']= data['platformName']
desired_caps['platformVersion']= data['platformVersion']
desired_caps['deviceName']= data['deviceName']

desired_caps['app']= data['app']
desired_caps['noReset']= data['noReset']
desired_caps['appPackage']= data['appPackage']
desired_caps['appActicity']= data['appActicity']
desired_caps['ip']= data['ip']
desired_caps['port']= data['port']

driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)