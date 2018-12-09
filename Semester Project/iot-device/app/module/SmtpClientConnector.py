from app.common import ConfigUtil,ConfigConst
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

 
class SmtpClientConnector():
    config         = ConfigUtil.ConfigUtil('/home/pi/workspace/iot-device/Lab1/iot-device/data/ConnectedDevicesConfig.props')
    enableEmulator = config.getProperty(ConfigConst.DEVICE, ConfigConst.ENABLE_EMULATOR_KEY)
    pollCycleSecs  = int(config.getProperty(ConfigConst.DEVICE, ConfigConst.POLL_CYCLES_KEY))
    nominalTemp    = int(config.getProperty(ConfigConst.DEVICE, ConfigConst.NOMINAL_TEMP_KEY))   
    
    def __init__(self):
        self.config.loadConfig()
        print('Configuration data...\n' + str(self.config))
 
    def publishMessage(self, topic, data):
        host     = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.HOST_KEY)
        port     = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.PORT_KEY)
        
        fromAddr = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.FROM_ADDRESS_KEY)
        toAddr   = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.TO_ADDRESS_KEY)
        authToken = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.USER_AUTH_TOKEN_KEY)
        

       
        msg = MIMEMultipart()
        msg['From'] = fromAddr
        msg['To'] = toAddr
        msg['Subject'] = topic
        msgBody = str(data)
        msg.attach(MIMEText(msgBody))
        
        msgText = msg.as_string()
    # send e-mail notification
        smtpServer = smtplib.SMTP_SSL(host, port)
        smtpServer.ehlo() 
        smtpServer.login(fromAddr, authToken)
        smtpServer.sendmail(fromAddr, toAddr, msgText)
        smtpServer.close()