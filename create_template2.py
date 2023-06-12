import boto3
from setting import AK, SK, REGION


def create_email_template(template_name, subject, body):
    # 创建 SES 客户端
    client = boto3.client('ses', region_name=REGION,
    aws_access_key_id=AK,
    aws_secret_access_key=SK)  

    # 创建模板
    response = client.create_template(
        Template={
            'TemplateName': template_name,
            'SubjectPart': subject,
            'TextPart': body
        }
    )

    # 打印模板创建结果
    print("Template created! Template Name: {}".format(response))

# 使用示例
template_name = 'Template4'
subject = 'Hello {{name}}!'
body = '''Dear {{name}},
Thank you for your interest in our product. We are pleased to inform you that we are offering a special discount of {{discount}}% on your next purchase. This offer is valid until {{expiry_date}}.

Sincerely,
Your Company'''

create_email_template(template_name, subject, body)
