import datetime
import os
import requests
import webbrowser

# 티스토리 주소 앞 (예시 : API_use.tistory.com 에서 API_use)
blog_name = "XXXX"

# redirect_uri는 앱등록할때 사용한 티스토리 주소를 사용합니다. 토큰 발행시 맨뒤에 /는 넣지 않습니다.
redirect_uri = "https://XXXX.tistory.com/"

# client_id는 app_id를 입력합니다.
Client_id = '8a16e0b49XXXXXX'
# client_secret = Secret_Key를 입력합니다. 
Secret_Key = '8a1XXXXXX'

# 인증 요청 및 Authentication code 발급 URL
# https://www.tistory.com/oauth/authorize?client_id={Client-id}&redirect_uri={redirect-uri}&response_type=code&state={state-param}

# code 는 access_token 을 받기 위한 중간 인증코드입니다. 한번 사용하면 재발급 받아야 합니다. 
Code = 'e28f59XXXXXXXXXXXXXXXXXXXXXXXXXX'


#임의의 문자열 (입력하지 않아도 됩니다.)
state_param = '' 
output_type = "xml"


access_token = ''

# 액세스 토큰 발급
if access_token == '' :
    get_token_url = f'https://www.tistory.com/oauth/access_token?client_id={Client_id}&client_secret={Secret_Key}&redirect_uri={redirect_uri}&code={Code}&grant_type=authorization_code'
    webbrowser.open(get_token_url)
    access_token = requests.get(get_token_url)
    print(access_token.text)

# access_token 발급 완료 ! 
# access_token = token.text[23:]

# print(access_token)