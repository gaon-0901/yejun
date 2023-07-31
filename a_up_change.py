def capitalize_first_a(name):
    if "a" in name:
        first_a_index = name.index("a")  # 첫 번째 "a"의 인덱스를 찾습니다.
        name = name[:first_a_index] + "A" + name[first_a_index + 1:]  # 첫 번째 "a"를 "A"로 바꿉니다.
    else:
        raise ValueError("입력한 문자열에 'a'가 없습니다.")
    return name

if __name__ == "__main__":
    name = input("문자열을 입력하세요: ")

    try:
        result = capitalize_first_a(name)
        print("첫 번째 'a'가 대문자 'A'로 바뀐 결과:", result)
    except ValueError as e:
        print("오류 발생:", e)
