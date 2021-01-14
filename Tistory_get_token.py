import datetime
import os
import requests
import webbrowser

# 티스토리 주소 앞 (예시 : API_use.tistory.com 에서 API_use)
blog_name = "API_use"

# redirect_uri는 앱등록할때 사용한 티스토리 주소를 사용합니다. 토큰 발행시 맨뒤에 /는 넣지 않습니다.
redirect_uri = "https://API_use.tistory.com/"

# client_id는 app_id를 입력합니다.
Client_id = 'XXXXXXXXXX'
# client_secret = Secret_Key를 입력합니다. 
Secret_Key = "ac3XXXXXXXXXXXXXXX"



# code 는 access_token 을 받기 위한 중간 인증코드입니다. 한번 사용하면 재발급 받아야 합니다. 
Code = '각자의 코드 ! '


#임의의 문자열 (입력하지 않아도 됩니다.)
state_param = '' 
output_type = "xml"


access_token = ''

# 액세스 토큰 발급
if access_token == '' :
    print('acess token 시도중...')
    token_url = f'https://www.tistory.com/oauth/access_token?client_id={client_id}&client_secret={Secret_Key}&redirect_uri={redirect_uri}&code={code}&grant_type=authorization_code'
    webbrowser.open(token_url)
    token = requests.get(token_url)
    print(token.text)
    
    # access_token 발급 완료 ! 
    # access_token = token[23:]