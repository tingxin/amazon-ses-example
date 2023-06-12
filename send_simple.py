import boto3
from setting import AK, SK, REGION


def send_email(sender, recipient, subject, body):
    # 创建 SES 客户端
    client = boto3.client('ses', region_name=REGION,
    aws_access_key_id=AK,
    aws_secret_access_key=SK)  

    # 发送邮件
    response = client.send_email(
        Source=sender,
        Destination={
            'ToAddresses': [
                recipient,
            ]
        },
        Message={
            'Subject': {
                'Data': subject
            },
            'Body': {
                'Text': {
                    'Data': body
                }
            }
        }
    )

    # 打印发送结果p
    print("Email sent! Message ID: {}".format(response['MessageId']))

# 使用示例
sender = 'tingxinxu@nwcdcloud.cn'
recipient = 'friendship-119@163.com'
subject = 'Hello from Amazon SES'
body = 'This is the body of the email.'

send_email(sender, recipient, subject, body)
