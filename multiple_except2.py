my_list=[1,2,3]

try: #문제가 없을 경우 실행할 코드

    print("첨자를 입력하세요:")
    index=int(input())
    print(my_list[index]/0)

except ZeroDivisionError as err: #문제가 생겼을 때 실행할 코드
    print("0으로 나눌 수 없습니다, ({0})".format(err))

except IndentationError as err: #문제가 생겼을 때 실행할 코드
    print("잘못된 첨자입니다. ({0})".format(err))