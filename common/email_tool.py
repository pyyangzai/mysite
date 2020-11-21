import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import zipfile
import os
from Common.common_function import get_current_dir
from Common.log import log
import socket


def zip_dir(skip_img=True):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    filename = get_current_dir('report.zip')
    zip = zipfile.ZipFile(filename, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(get_current_dir('Test_Report')):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(get_current_dir('Test_Report'), '')
        if 'img' in dirnames:
            if skip_img:
                dirnames.remove('img')
        for name in filenames:
            zip.write(os.path.join(path, name), os.path.join(fpath, name))
    zip.close()
    return filename


def getAttachment(attachmentFilePath):
    attachment = MIMEText(open(attachmentFilePath, 'rb').read(), 'base64', 'utf-8')
    attachment["Content-Type"] = 'application/octet-stream'
    attachment["Content-Disposition"] = 'attachment;filename=%s' % os.path.basename(attachmentFilePath)
    return attachment


def send_mail(recipient, subject='Automation Report Linux', text='', attachment=''):
    mailUser = "AutomationTest<AutoTest@hp.com>"
    msg = MIMEMultipart('related')
    msg['From'] = mailUser
    msg['To'] = ','.join(recipient)
    msg['Subject'] = subject  # "AddonCatalog check result"
    msg.attach(MIMEText(text, 'html', 'utf-8'))


    msg.attach(getAttachment(attachment))
    print(attachment)
    try:
        mailServer = smtplib.SMTP(host='smtp1.hp.com', port=25, local_hostname=socket.gethostname())
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.sendmail(mailUser, recipient, msg.as_string())
        mailServer.close()
        print("Sent email to %s success" % recipient)
    except:
        import traceback
        log.info(traceback.format_exc())


if __name__ == "__main__":
    # main(sys.argv)
    zip_dir()
    pass
