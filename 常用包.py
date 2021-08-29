
# 第三方库
# 解析html解析器
from lxml import etree

import ssl
# 全局去除证书验证
ssl._create_default_https_context = ssl._create_unverified_context