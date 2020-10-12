import os

class Config:
    SECRET_KEY = '5ed25becb3b0a153dbe985e8ccf76764' #move this also to os
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' #move this also to os
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')