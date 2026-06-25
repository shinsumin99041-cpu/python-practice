#문자열 처리 함수
python="Python is Amazing"
print(python.lower()) # python 이라는 변수 안에 지금 대문자 P와 A가 있는데, lower()함수를 써서 모두 다 소문자로 출력
print(python.upper()) # upper()함수를 이용해서 모두 다 대문자로 출력
print(python[0].isupper()) # isupper() 함수를 이용해서 첫번째 글자가 대문자인지 확인하는 것. []인덱스 안에 있는 번호는 알아서 바꾸면 된다. but, 맨처음은 항상 0번부터 시작이다.
print(len(python)) # len() 함수를 이용해서 python 전체 문자열의 길이를 반환 해 준다. -> 얘는 길이가 17로 나옴
print(python.replace("Python", "Java")) # replace() 함수를 이용해서 전체 문장 중에서 Python이라는 글자를 찾아서 저 글자를 Java로 바꿔서 출력

index=python.index("n") # 어떤 문자가 어느 위치에 있는지도 확인가능하다.but, 여러개의 n이 있을 경우 가장 앞에 있는거를 찾아줌 -> 얘는 5가 나온다.
print(index)
index=python.index("n",index+1) # 이렇게 해주면 앞에서 찾은 위치의 다음부터 찾아줄 수 있다. -> 얘는 15가 나온다.
print(index)

print(python.find("n")) # 원하는 문자를 괄호 안에 넣으면 이 문자가 있는 위치를 알려준다. -> 얘도 첫번째로 나오는 위치
print(python.find("Java")) # Java라는 문자가 없는데, 쓰면 값이 -1이 나온다. 즉 괄호 안의 문자가 변수 안에 포함이 안되어 있으면 -1이 반환된다.
#print(python.index("Java")) # -> 이 상황은 오류가 난다. python이라는 변수안에는 Java가 없기 때문에 그냥 에러를 내버리는거다.
# 즉, find에서는 원하는 값이 없을 경우 -1로 반환을 해주고, index에서는 원하는 값이 없을 경우 그냥 오류가 나면서 프로그램을 종료해버린다. 즉 이 상황에서 index 부분에서 오류가 나면 뒤에 어떤걸 쓰던, 출력이 되지 않는다. 
print("hi") # -> 위에서 index 부분에서 오류가 나면서 프로그램을 종료했기 때문에 뒤에 어떠한 것도 출력되지 않는다. 

print(python.count("")) # python이라는 변수에서 n이 총 몇번 등장하는지 알려준다. -> 스펠링뿐만 아니라 단어도 된다.

#문자열 포맷 
print("a" + "b") # 출력: ab  => (원래했던 방식)
print("a", "b") # 출력: a b   => (원래했던 방식) ... 

#방법1 [%d, %s, %c]
print("나는 %d살입니다." %20) # %d 위치에 20을 넣겠다는 의미 -> %d는 정수를 의미
print("나는 %s을 좋아해요." %"파이썬")  # %s 위치에 파이썬을 넣겠다는 의미(파이썬은 문자형이므로 "" 이거 해줘야 한다) -> %s는 문자를 의미
print("Apple 은 %c로 시작해요." %"A") # %c 위치에 A를 넣겠다는 의미 -> %c는 한 글자만 받겠다는 의미
# %s로 쓸 경우 정수든, 문자 하나든 다 가능하다.
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

#방법2 [.format()]
print("나는 {}살입니다." .format(20)) # .format()여기서 괄호안에 있는것이 {}안에 들어간다는 의미
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간")) # -> 0번째에 있는 파란이 0번째인 앞에 들어가고, 1번째에 있는 빨간이 1번째인 뒤에 들어간다는 의미.
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간")) # -> 0번째에 있는 파란이 0번째인 뒤에 들어가고, 1번째에 있는 빨간이 1번째인 앞에 들어간다는 의미.

#방법3 [하나의 문장 속에 변수 선언하기]
print("나는 {age}살이며, {color}색을 좋아해요." .format(age=20, color="빨간")) 
print("나는 {age}살이며, {color}색을 좋아해요." .format(color="빨간", age=20)) 

#방법4 [직접 변수 만들어 사용. print문 내에서 f로 시작을 한다.]
age = 20
color="빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출 문자 (\n, \, \\, \r, \b, \t)
print("백문이 불여일견 백견이 불여일타") # 이 문장을 두 줄로 쓰고싶다면? 
print("백문이 불여일견\n백견이 불여일타") # 탈출문자인 \n을 쓰면 된다. -> \n:줄바꿈

#저는 "나도코딩"입니다.
# print("저는 "나도코딩"입니다.") # -> 얘는 오류뜸. wht? 파이썬에서 ""는 하나의 문자열로 인식하기 때문 
print("저는 '나도코딩'입니다.") # 작은따옴표를 사용하면 가능. 하지만 우리가 원하는건 "나도코딩" 이렇게 나와야 한다.
print('저는 "나도코딩"입니다.') # 그럼 작은따옴표와 큰따옴표 위치를 바꾸면 된다.
#탈출문자를 이용하는 방법도 있다!
print("저는 \"나도코딩\"입니다.") #큰따옴표(작은따옴표) 앞에 각각 \붙여주기

# \\ : 문장 내에서는 \로 바뀌게 된다.
# print("C:\Users\sumin\OneDrive\문서\Desktop\PythonWorkspace\.venv>") -> 오류뜬다. \이게 하나씩 있기 때문
print("C:\\Users\\sumin\\OneDrive\\문서\\Desktop\\PythonWorkspace\\.venv>") # \하나씩 더 추가해면 된다.

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # 결과 -> Pine Apple => 맨 앞에 Red부분을 Pine이 커서를 맨 앞으로 이동해서 저 부분을 Pine로 대신 써준다.

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple") # 결과 -> RedApple 

# \t : 탭
print("Red\tApple") # 결과 -> Red     Apple

#퀴즈3 사이트별로 비민번호를 만들어 주는 프로그램을 작성하시오. 
# 예) http://naver.com
# 규칙1: http:// 부분은 제외 => naver.com
# 규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                (nav)             (5)            (1)          (!) 
# 예) 생성된 비밀번호 : nav51!

url= "http://naver.com"
my_str = url.replace("http://","") # 짜르는 값을 my_str변수로 설정. replace를 이용해 http://를 빈칸으로 바꿈 => 규칙1
print(my_str) 
my_str=my_str[0:5] # 0부터 5직전까지 출력. -> my_str=my_str[:my_str.index(".")] 이렇게도 가능 => 규칙2
print(my_str)
password=my_str[0:3]+str(len(my_str)) + str(my_str.count("e")) +"!" # len 와 count는 정수형인데, 앞에 문자형과 합쳐야 하므로 str로 묶어줘야 한다.
print("{}의 비밀번호는 {}입니다." .format(url, password))

#리스트[] -> 순서를 가지는 개체의 집합
# ex) 지하철 칸별로 10명, 20명, 30명
# subway1=10
# subway2=20
# subway3=30
# ->이렇게 각각의 변수를 정해 적었었는데, 리스트는 이것들을 이제 하나로 연속적인 공간에 묶는다는 것이다.
subway=[10,20,30] # 리스트를 이용해 하나로 묶으면 된다.
print(subway) # 결과 -> [10, 20, 30]

subway=["유재석","조세호","박명수"]
print(subway)

print(subway.index("조세호")) #조세호씨가 몇번째 칸에 타고있는지 알 수 있다. 

#하하가 다음 정류장에서 다음 칸에 탐. 
subway.append("하하") #append는 맨 뒤에 더하다라는 의미
print(subway) # 결과 -> ['유재석', '조세호', '박명수', '하하']

#정형돈씨를 유재석과 조세호 사이에 태워봄
subway.insert(1,"정형돈") # insert를 이용해서 인덱스1번째 자리(즉, 조세호자리)에 정형돈이 들어가면 된다. 항상 먼저 어느 자리에 넣을건지를 먼저 앞에 적어줘야 한다. 
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄. 
print(subway.pop()) # 결과 -> 하하 / pop함수는 뒤에서부터 하나씩 꺼내는 함수이다.
print(subway) # 결과 -> ['유재석', '정형돈', '조세호', '박명수']
print(subway.pop()) # 결과 -> 박명수
print(subway) # 결과 -> ['유재석', '정형돈', '조세호']
print(subway.pop()) # 결과 -> 조세호
print(subway) # 결과 -> ['유재석', '정형돈']

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway) # 결과 -> ['유재석', '정형돈', '유재석'] 
print(subway.count("유재석")) # 결과 -> 2

#정렬도 가능
num_list=[5,2,4,3,1] 
num_list.sort() # sort는 정렬한다는 의미
print(num_list) # 결과 -> [1, 2, 3, 4, 5]

#순서 뒤집기 가능
num_list.reverse() # reverse는 순서를 뒤집는다는 의미
print(num_list) # 결과 -> [5, 4, 3, 2, 1]

#모두 지우기
num_list.clear() #num_list 안에 있는 내용을 모두 삭제한다는 의미
print(num_list) # 결과 -> []

#다양한 자료형 함꼐 사용
mix_list=["조세호",20,True]
print(mix_list) # 결과 -> ['조세호', 20, True]

#리스트 확장도 가능 (하나의 리스트로 합치는 것)
num_list=[5,2,4,3,1] 
mix_list=["조세호",20,True]
num_list.extend(mix_list) # extend 리스트 확장해주는 함수
print(num_list) # 결과 ->  [5, 2, 4, 3, 1, '조세호', 20, True]