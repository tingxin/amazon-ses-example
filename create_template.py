import boto3
from setting import AK, SK, REGION


def create_template(template_name, subject_part, text_part, html_part):
    # 创建 SES 客户端
    client = boto3.client('ses', region_name=REGION,
    aws_access_key_id=AK,
    aws_secret_access_key=SK)  

    # 创建模板
    response = client.create_template(
        Template={
            'TemplateName': template_name,
            'SubjectPart': subject_part,
            'TextPart': text_part,
            'HtmlPart': html_part
        }
    )

    # 打印模板创建结果
    print("Template created! Template Name: {}".format(response))

# 使用示例
template_name = 'MyTemplate'
subject_part = 'Hello {{name}}!'
text_part = 'Hello {{name}}! This is the text part of the email.'
html_part = '<html><body><h1>Hello {{name}}!</h1><p>This is the HTML part of the email.</p></body></html>'

create_template(template_name, subject_part, text_part, html_part)
