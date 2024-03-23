import requests
import re
import urllib.parse


def download_pdf(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(8192):
                if chunk:
                    f.write(chunk)
        print(f"PDF downloaded successfully and saved to {save_path}")

    except Exception as exc:
        print(exc)

def get_url(url):
    pattern = re.compile(r'contentId=(.*?)&catalogType=')
    match = pattern.search(url)
    if match:
        content_id = match.group(1)
        download_url = f"https://r2-ndr.ykt.cbern.com.cn/edu_product/esp/assets/{content_id}.pkg/pdf.pdf"
        return download_url
    else:
        return "No match found."



url = 'https://example.com/'
save_path = r'output.pdf'

download_url = get_url(url)
download_pdf(download_url, save_path)