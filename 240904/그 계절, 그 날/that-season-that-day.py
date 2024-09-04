def is_leap_year(year):
    # 윤년인지 아닌지 판단하는 함수
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def is_valid_date(year, month, day):
    # 월별 최대 일수 정의
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31,
        6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
        11: 30, 12: 31
    }
    
    # 윤년이면 2월은 29일까지 가능
    if is_leap_year(year):
        days_in_month[2] = 29
    
    # 주어진 월과 일자가 유효한지 판단
    if 1 <= month <= 12 and 1 <= day <= days_in_month[month]:
        return True
    else:
        return False

def find_season(month):
    # 월에 따른 계절 출력
    if 3 <= month <= 5:
        return "Spring"
    elif 6 <= month <= 8:
        return "Summer"
    elif 9 <= month <= 11:
        return "Fall"
    else:  # 12, 1, 2월인 경우
        return "Winter"

def main():
    Y, M, D = map(int, input().split())
    
    if is_valid_date(Y, M, D):
        print(find_season(M))
    else:
        print(-1)

main()