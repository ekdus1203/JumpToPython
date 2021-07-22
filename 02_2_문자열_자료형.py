#문자열을 만들 때 큰따옴표만을 사용했지만 이 외에도 문자열을 만드는 방법은
#3가지가 더 있다. 파이썬에서 문자열을 만드는 방법은 총 4가지이다.

#1.큰따옴표(")로 양쪽 둘러싸기
"Hello World"
#2.작은따옴표(')로 양쪽 둘러싸기
'Phthon is fun'
#3.큰따옴표 3개를 연속(""")으로 써서 양쪽 둘러싸기
"""Life is too short, You need python"""
#4.작은따옴표 3개를 연속(''')으로 써서 양쪽 둘러싸기
'''Life is too short, You need python'''
#단순함이 자랑인 파이썬이 문자열을 만드는 방법은 왜 4가지나 가지게 됐을까? 그 이유를 알아보자

#문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때
#문자열을 만들어 주는 주인공은 작은따옴표(')와 큰따옴표(")이다. 그런데 문자열 안에도 작은따옴표와
#큰따옴표가 들어 있어야 할 경우가 있다. 이때는 좀 더 특별한 기술이 필요하다.

#1.문자열에 작은따옴표(') 포함시키기
#Python's favorite food is perl
#위와 같은 문자열을 food 변수에 저장하고 싶다고 가정하자. 문자열 중 Python's에 작은 따옴표가(')가 포함
#이럴 때는 다음과 같이 문자열을 큰따옴표(")로 둘러싸야한다. 큰따옴표 안에 들어있는 작은따옴표는 문자열을
#나타내기 위한 기호로 인식되지 않는다.
food = "Python's favorite food is perl"

#프롬포트에 food를 입역해서 결과를 확인하자. 변수에 저장된 문자열이 그대로 출력되는 것을 볼 수 있다.
food
"Python's favorite food is perl"
#시험 삼아 다음과 같이 큰따옴표(")가 아닌 작은따옴표(')로 문자열을 둘러싼 후 다시 실행해보자.
#'Python'이 문자열로 인식되어 구문 오류가 발생할 것이다.
    food = 'Python's favorite food is perl'
File "<stdin>", line 1
    food = 'Python's favorite food is perl'
                ^
SyntaxError : invalid syntax

#2.문자열에 큰따옴표(") 포함시키기
"Python is very easy." he say.
#위와 같이 큰따옴표(")가 포함된 문자열이라면 어떻게 해야 큰따옴표가 제대로 표현될까?
#다음과 같이 문자열을 작은따옴표(')로 둘러싸면 된다.\
say = '"Python is very easy." he says.'
#이렇게 작은따옴표(') 안에 사용된 큰따옴표는(")는 문자열을 만드는 기호로 인식되지 않는다.

#3.백슬래시(|)를 사용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

#작은따옴표나 큰따옴표를 문자열에 포함시키는 또 다른 방법은 백슬래시를 사용하는 것이다.
#즉, 백슬래시를 작은따옴표나 큰따옴표 앞에 삽입하면 백슬래시 뒤의 작은따옴표나 큰따옴표는 문자열을
#둘러싸는 기회의 의미가 아니라 문자('),(") 그 자체를 뜻하게 된다.
#어떤 방법을 사용해서 문자열 안에 작은따옴표와 큰따옴표를 포함시킬지는 각자의 선택이다.

#여러 줄인 문자열을 변수에 대입하고 싶을 때 - 문자열이 항상 한 줄짜리만 있는 것은 아니다.
#다음과 같이 여러 줄의 문자열을 변수에 대입하려면 어떻게 처리해야 할까?
Life is too short
You need python

#1.줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기
multiline = "Life is too short\n You need python"
#위 예처럼 줄바꿈 문자 \n을 삽입하는 방법이 있지만 읽기에 불편하고 줄이 길어지는 단점이 있다.

#2.연속된 작은따옴표 3개(''') 또는 큰따옴표(""") 사용하기
#위 1번의 단점을 극복하기 위해 파이썬에서는 다음과 같이 작은따음표 3개(''') 또는 큰따옴표(""")를 사용
multiline='''
          Life is too short
          You need python
          ''' #작은따옴표 3개를 사용한 경우
multiline="""
          Life is too short
          You need python
          """ #큰따옴표 3개를 사용한 경우
#출력결과물 print(multiline)
#         Line is too short
#         You need python

#두 경우 모두 결과는 동일하다. 위 예에서도 확인할 수 있듯이 문자열이 여러 줄인 경우 이스케이프
#코드를 쓰는 것보다 따옴표를 연속해서 쓰는 것이 더 깔끔하다.

#[이스케이프 코드란] - 문자열 예제에서 여러 줄의 문장을 처리할 때 백슬래시 문자와 소문자 n을 조합한 \n
#이스케이프 코드를 사용했다. 이스케이프 코드란 프로그래밍할 때 사용 할 수 있도록 미리 정의해둔 "문자조합"이다.
#주록 출력물을 보기 좋게 정렬하는 용도로 사용. 몇 가지 이스케이프 코드를 정리하면 다음과 같음
#\n : 문자열 안에서 줄을 바꿀 때 사용
#\t : 문자열 사이에 탭 간격을 줄 때 사용
#\\ : 문자 \를 그대로 표현할 때 사용
#\' : 작은따옴표(')를 그대로 표현할 때 사용
#\" : 큰따옴표를 그대로 표현할 때 사용
#\r : 캐리지 리턴(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
#\f : 폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
#\a : 벨 소리(출력할 때 PC스피커에서 '삑' 소리가 난다)
#\b : 백 스페이스
#\000 : 널 문자
#이 중에서 활용빈도가 높은 것은 \n, \t, \\, \',\"임. 나머지 잘 사용ㄴㄴ

#문자열 연산하기
#파이썬에서는 문자열을 더하거나 곱할 수 있다. 다른 언어에서는 쉽게 찾아볼 수 없는 재밌는 기능으로,
#우리 생각을 그대로 반영해주는 파이썬만의 장점이라고 할 수 있다.

#문자열 더해서 연결하기
head = "Python"
tail = "is fun!"
head + tail
'Python is fun!'

#위 소스 코드에서 세번째 줄을 보자. 복잡하게 생각하지 말고 눈에 보이는 대로 생각해보자.
#"Python"이라는 head 변수와 "is fun!"이라는 tail 변수를 더한 것이다. 결과는 'Python is fun!'이다.
#즉, head 와 tail 변수가 + 에 의해 합쳐진 것이다.

#문자열 곱하기
a="Python"
a*2
'PythonPython'

#위 소스 코드에서 *의 의미는 우리가 일반적으로 사용하는 숫자 곱하기의 의미와는 다르다.
#위 소스 코드에서 a*2 문장은 a를 두 번 반복하라는 뜻이다. 즉 * 는 문자열의 반복을 뜻하는 의미로 사용
#굳이 코드의 의미를 설명할 필요가 없을 정도로 직관적

#문자열 곱하기 응용 - 다음 소스를 IDLE 에디터를 열고 작성해 보자.
#multistring.py
print("="*50)
print("My Program")
print("="*50)

#입력한 소스는 C:\doit 디렉터리에 파일 이름 multistring.py로 저장하자.
#이제 프로그램 실행 > [윈도우 + R(실행) > cmd 입력 > Enter ]를 눌러 명령 프롬프트 창 열고 따라해보자
#결과값이 다음과 같을 것이다.
C:\Users>cd C:\doit
C:\doit>python multistring.py
==================================
My Program
==================================

#문자열 길이 구하기
#문자열의 길이는 다음과 같이 len 함수를 사용하면 구할 수 있다. len 함수는 print 함수처럼
#파이썬의 기본 내장 함수로 별다른 설정 없이 바로 사용할 수 있다.
a = "Life is too short"
len(a)
17

#문자열 인덱싱과 슬라이싱
#인덱싱이란 무엇인가를 '가리킨다'는 의미, 슬라이싱은 무엇인가를 '잘라낸다'

#문자열 인덱싱이란
a = "Life is too short, You need Python"
#위 소스 코드에서 변수 a에 저장한 문자열의 각 문자마다 번호를 매겨 보면 다음과 같다
Life is too short, You need Python
0         1         2         3
0123456789012345678901234567890123
#"Life is too short, You need Python" 문자열에서 L은 첫번째 자리를 뜻하는 숫자 0,
#바로 다음인 i는 1 이런 식으로 계속 번호를 붙인 것이다. 중간에 있는 short의 s는 12가 된다.
a="Life is too short, You need Python"
a[3]
'e'
#a[3]이 뜻하는 것은 a라는 문자열의 네 번째 문자 e를 말한다. 파이썬은 0부터 숫자를 센다

#문자열 인덱싱 활용하기
a = "Life is too short, You need Python"
a[0] = 'L'
a[12] = 's'
a[-1] = 'n'
a[-0] = 'L'
a[-2] = 'o'
a[-5] = 'y'

#문자열 슬라이싱 - 한 문자 아니고 단어 뽑아내기
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
b
'Life'

a = "Life is too short, You need Python"
a[0:4]
'Life'

a[0:3]
'Lif'

0 <= a < 3

#문자열을 슬라이싱하는 방법
a[0:5]
'Life '

#항상 시작 번호가 0일 필요는 없다.
a[0:2]
'Li'

a[5:7]
'is'

a[12:17]
'short'

#a[시작번호:끝번호]에서 끝 번호 부분을 생락햐면 시작 번호부터 그 문자열의 끝까지 뽑아낸다.
a[19:]
'You need Python'

#a[시작번호:끝번호]에서 시작 번호를 생략하면 문자열의 처음부터 끝 번호까지 뽑아낸다.
a[:17]
'life is too short'

#a[시작번호:끝번호]에서 시작 번호와 끝 번호를 생략하면 문자열의 처음부터 끝까지 뽑아낸다.
a[:]
'life is to short, You need Python'

#슬라이싱에서도 인덱싱과 마찬가지로 마이너스(-) 기호를 사용할 수 있다.
a[19:-7]
'You need'

#슬라이싱으로 문자열 나누기
a="20010331Rainy"
date = a[:8]
weather = a[8:]
date
'20010331'
weather
'Rainy'

a = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
year
'2001'
day
'0331'
weather
'Rainy'

# Pithon > Python
a = "Pithon"
a[1]
'i'
a[1]='y' #오류오류!

a = "Pithon"
a[:1]
'P'
a[2:]
'thon'
a[:1] + 'y' + a[2:]
'Python'

#문자열 포매팅

#문자열 포매팅 따라하기
#1. 숫자 바로 대입
"I eat %d apples."%3
'I eat five apples.'

#2.문자열 바로 대입
"I eat %s apples." % "five"
'I eat five apples.'

#3.숫자 값을 나타내는 변수로 대입
number = 3
"I eat %d apples." % number
'I eat 3 apples'

#4.2개 이상의 값 넣기
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)
'I ate 10 apples. so I was sick for three days.'

#문자열 포멧 코드
# %s:문자열, %c:문자1개, %d:정수, %f:부동소수, %o:8진수, %x:16진수, %%:Literal(문자%자체)
#%%는 어떤 형태의 값이든 변환해 넣을 수 있다.
"I have %s apples"%3
'I have 3 apples'
"rate is %s"%3.234
'rate is 3.234'

#[포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다]
"Error is %d%." % 98 < 오류남!
"Error is %d%%."%98
'Error is 98%'

#포맷 코드와 숫자 함께 사용하기

#1.정렬과 공백
"%10s"%"hi"
'        hi'
"%-10sjane."%'hi'
'hi    jane.'

#2.소수점 표현하기
"%0.4f"%3.42134234
'3.4213'
"%10.4f"%3.42134234
'    3.4213'

#format 함수를 사용한 포매팅
#숫자 바로 대입하기
"I eat {0} apples".format(3)
'I eat 3 apples'

#문자열 바로 대입하기
"I eat {0} apples".format("five")
'I eat five apples'

#숫자 값을 가진 변수로 대입하기
number = 3
"I eat {0} apples".format(number)
'I eat 3 apples'

#2개 이상의 값 넣기
number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number,day)
'i ate 10 apples. so I was sick for three days.'

#이름으로 넣기
f"I ate {number} apples. so I was sick for {day} days.".format(number=10,day=3)
'I ate 10 apples. so I was sick for 3 days.'

#인덱스와 이름을 혼용해서 넣기
f"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
'I ate 10 apples. so I was sick for 3 days.'

#왼쪽 정렬
"{0:<10}".format("hi")
'hi        ' #치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자리수를 10으로 맞춤

#오른쪽 정렬
"{0:>10}".format("hi")
'       hi'

#가운데 정렬
"{0:^10}".format("hi")
'    hi    '

#공백 채우기
"{0:=^10}".format("hi")
'====hi===='
"{0:!<10}".format("hi")
'hi!!!!!!!!'

#소수점 표현하기
y = 3.42134234
"{0:0.4f}".format(y)
'3.4213'
"{0:10.4f}".format(y)
'    3.4213'

#{또는} 문자 표현하기
"{{ and }}".format()
'{ and }'

#f문자열 포매팅
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'

age = 30
f'나는 내년이면 {age+1}살이 된다.'
'나는 내년이면 31살이 된다.'

d = {'name':'홍길동','age':30}
f'나의 이름은 {d["name"]}입니다.나이는 {d["age"]}입니다.'
'나의 이름은 홍길동입니다. 나이는 30 입니다.'

f'{"hi:<10"}' #왼쪽정렬
'hi          '
f'{"hi":>10}' #오른쪽정렬
'        hi'
f'{"hi:^10"}' #가운데정렬
'    hi    '
f'{"hi:=^10"}' #가운데 정렬하고 '=' 문자로 공백 채우기
'====hi===='
f'{"hi:!<10"}' #왼족 정렬하고 '!' 문자로 공백 채우기
'hi!!!!!!!!'

y = 3.42134234
f'{y:0.4f}' #소수점 4자리까지만 표현
'3.4213'
f'{y:10.4f}' #소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤
'    3.4213'
f'{{ and }}'
'{ and }'

#문자열 관련 함수들

#문자 개수 세기(count)
a="hobby"
a.count('b')
2

#위치 알려주기1
a = "Python is the best choice"
a.find('b')
14
a.find('k')
-1