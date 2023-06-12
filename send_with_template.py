import boto3
from setting import AK, SK, REGION

def send_email_with_template(sender, recipient, template_name, template_data):
    # 创建 SES 客户端
    client = boto3.client('ses', region_name=REGION,
    aws_access_key_id=AK,
    aws_secret_access_key=SK)  


    # 发送邮件
    response = client.send_templated_email(
        Source=sender,
        Destination={
            'ToAddresses': [
                recipient,
            ]
        },
        Template=template_name,
        TemplateData=template_data
    )

    # 打印发送结果
    print("Email sent! Message ID: {}".format(response))

# 使用示例
sender = 'tingxinxu@nwcdcloud.cn'
recipient = 'friendship-119@163.com'
template_name = 'MyTemplate'
template_data = '{"name": "John"}'

send_email_with_template(sender, recipient, template_name, template_data)
