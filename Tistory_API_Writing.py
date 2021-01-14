from bs4 import BeautifulSoup
import requests

# 앞에서 획득한 token 사용 
access_token = ''

# 티스토리 주소가 abcd1.tistory.com 이라고 가정
blog_name = 'abcd1'

# 게시글 카테고리
categor = '0'

# 글쓰기 기능 API 함수 
def write_ti():
    url = 'https://www.tistory.com/apis/post/write'
    title = '티스토리 API 이용한 글쓰기 제목'
    content = '<h2 data-ke-size="size26"> <b>HTML 방식 제목2 글씨 </b>입니다.╰(*°▽°*)╯</h2>' +'<p>&nbsp;</p>'*2 
    
    # 이미지 추가 
    imgs = file_ti()
    for img in imgs:
        content += img

    # 파라미터들
    params = {

        'access_token': access_token,

        'output': 'json',

        'blogName': blog_name ,

        'title': title,

        'content':  content,

        'visibility': '3', # 공개 발행

        'category': categor, 

        'tag': 'tag1, tag12 , tag123',

        'acceptComment': '1'  # 댓글 허용

    }
    resp = requests.post(url, params=params)
    # soup = BeautifulSoup(resp.text)
    # print(soup.prettify())
    print(resp.text)

# 파일첨부 기능 API 함수
def file_ti():
    base_url2 = 'https://www.tistory.com/apis/post/attach?'
    parameters = {
                'access_token': access_token,
                'blogName': blog_name ,
                }

    # n개 사진 첨부하기. (첫 번째 사진이 대표사진)
    imgs,n = [],3
    for i in range(n)):
        file = {'uploadedfile': open(f'사진{i}.jpg','rb')}
        result = requests.post(base_url2, params=parameters, files= file)
        result = BeautifulSoup(result.text)
        result = result.prettify()
        # info_img = result[result.find('r>')+2:result.find('</replacer')]  이미지를 html 방식으로 바꾸어서 리스트에 추가하기 
        imgs.append(infos)
    return imgs
    
    #이미지 생성
def image_rp():
    img = Image.new("RGB",(460,600), (157,206,255))
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("./batang.ttc" , 40)
    d.text((20,100),'이미지 글씨', font=fnt, fill=(181,29,104))
    img.save('Draw_image.jpg')
    # img.show()
    return img


write_ti()