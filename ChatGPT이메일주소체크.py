import re

# 이메일 주소를 검사할 정규 표현식 패턴
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# 이메일 주소를 검사하는 함수
def is_valid_email(email):
    if re.match(email_pattern, email):
        return True
    else:
        return False

# 샘플 이메일 주소 리스트
sample_emails = [
    'example@example.com',
    'test.email@domain.co',
    'user+name@sub.domain.com',
    'invalid-email@domain',
    'user@domain@domain.com',
    'user@domain..com',
    'user@.com',
    'user@domain.c',
    'username@domain.com',
    'user@domain.com'
]

# 각 이메일 주소의 유효성을 검사하고 결과를 출력
for email in sample_emails:
    print(f'{email}: {"Valid" if is_valid_email(email) else "Invalid"}')
