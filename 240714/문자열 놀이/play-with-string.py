content, answer_num = map(str, input().split())
content = list(content)
answer_num = int(answer_num)

for i in range(answer_num):
    answer = list(input().split())
    if answer[0] == "1":
        # 인덱스 위치 변경
        storage = content[int(answer[1])-1]
        content[int(answer[1])-1] = content[int(answer[2])-1]
        content[int(answer[2])-1] = storage
        print(''.join(map(str, content)))
    else:
        # 문자 변경
        for i in range(len(content)):
            if content[i] == answer[1]:
                content[i] = answer[2]
        print(''.join(map(str, content)))