import re

def transform_text (text):

    phone_pattern = r"\b\d{5}[-]?\d{5}\b"
    text = re.sub(phone_pattern, "[REDACTED]", text)

    date_pattern = r"\b(\d{4})[-](\d{2})[-](\d{2})\b"
    month = {'01': "January", '02':'February', '03':"March", '04':'April', '05':'May', '06':'June', '07':'July', '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'}
    match = re.search(date_pattern,text)
    if match:
        text = re.sub(date_pattern, f"{match.group(3)} {month[match.group(2)]} {match.group(1)}", text)

    text = re.sub(r"\bpython\b", "🐍", text, flags=re.IGNORECASE)
    return text

def main():
    text = input("Enter a paragraph: ")
    print(transform_text(text))

main()