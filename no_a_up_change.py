name = input("a가 포함된 문자열: ")  # 사용자로부터 문자열을 입력받습니다.
name1 = name.index("a")  # "a"가 처음으로 나타나는 인덱스를 찾습니다.

# 문자열을 리스트로 변환하여 첫 번째 "a"를 대문자 "A"로 바꿉니다.
name_list = list(name)
name_list[name1] = name[name1].upper()

result = "".join(name_list)

print("첫 번째 'a'가 대문자 'A'로 바뀐 결과:", result)
