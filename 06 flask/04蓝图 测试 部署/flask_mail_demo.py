#coding:utf8

from flask import Flask
from flask_mail import Mail,Message
app = Flask(__name__)

# 配置邮件: 服务器 端口 传输安全协议 邮箱名 密码
app.config.update(
    DEBUG = True,
    MAIL_SERVER = 'smtp.qq.com',
    MAIL_PROT = 465,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = '625547721@qq.com',
    MAIL_PASSWORD = 'yuxuehui520',
)

mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Thes is a test',sender='625547721@qq.com', recipients=['lin_yi_0604@qq.com'])
    #邮件内容
    msg.body = 'flask test mail'
    print 'mail sent'
    return 'sent succeed'

if __name__ == '__main__':
    app.run()