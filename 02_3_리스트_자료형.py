02_3_리스트 자료형

odd = [1,3,5,7,9]

a = []
b = [1,2,3]
c = ['Life','is','too','short']
d = [1,2,'Life','is']
e = [1,2,['Life','is']]

#리스트의 인덱싱과 슬라이싱
#인덱싱
a=[1,2,3]
a
[1,2,3]

a[0]
1

a[0]+a[2]
4

a[-1]
3

a=[1,2,3['a','b','c']]

a[0]
1

a[-1]
['a','b','c']

a[3]
['a','b','c']

a[-1][0]
'a'

a[-1][1]
'b'

a[-1][2]
'c'

#[삼중 리스트에서 인덱싱하기]
a = [1,2['a','b',['Life','is']]]

a[2][2][0]
'Life'

#리스트의 슬라이싱
a=[1,2,3,4,5]
a[0:2]
[1,2]

a ="12345"
a[0:2]
'12'

a = [1,2,3,4,5]
b = a[:2]
c = a[2:]
b
[1,2]
c
[3,4,5]

[중첩된 리스트에서 슬라이싱하기]
a = [1,2,3,['a','b','c'],4,5]
a[2:5]
[3,['a','b','c'],4]
a[3][:2]
['a','b']

#리스트연산하기

#더하기
a = [1,2,3]
b = [4,5,6]
a + b
[1,2,3,4,5,6]

#반복하기
a = [1,2,3]
a * 3
[1,2,3,1,2,3,1,2,3]

#길이구하기
a = [1,2,3]
len(a)
3

#[초보자가 범하기 쉬운 리스트 연산 오류] - 형 오류

a = [1,2,3]
a[2] + "hi"

str(a[2]) + "hi"

#리스트의 수정과 삭제

#리스트에서 값 수정하기
a = [1,2,3]
a[2] = 4
a
[1,2,4]

#del 함수 사용해 리스트 요소 삭제하기
a = [1,2,3]
del a[1]
a
[1,3]

a = [1,2,3,4,5]
del a[2:]
a
[1,2]

#리스트 관련 함수들
#리스트에 요소 추가(append)
a= [1,2,3]
a.append(4)
a
[1,2,3,4]

a.append([5,6])
a
[1,2,3,4,[5,6]]

#리스트 정렬(sort)
a = [1,4,3,2]
a.sort()
a
[1,2,3,4]

a = ['a','c','b']
a.reverse()
a
['b','c','a']

#위치반환(index)
a = [1,2,3]
a.index(3)
2
a.index(1)
0

#리스트에 요소 삽입(insert)
a = [1,2,3]
a.insert(0,4)
a
[4,1,2,3]

a.insert(3,5)
a
[4,1,2,5,3]

#리스트 요소 제거(remove)
a = [1,2,3,1,2,3]
a.remove(3)
a
[1,2,1,2,3]

a.remove(3)
a
[1,2,1,2]

#리스트 요소 끄집어내기(pop)
a = [1,2,3]
a.pop(1)
2
a
[1,3]

a = [1,2,3]
a.pop(1)
2
a
[1,3]

#리스트에 포함된 요소 X의 개수 세기(count)
a = [1,2,3,1]
a.count(1)
2

#리스트 확장
a = [1,2,3]
a.extend([4,5])
a
[1,2,3,4,5]
b = [6,7]
a.extend(b)
a
[1,2,3,4,5,6,7]