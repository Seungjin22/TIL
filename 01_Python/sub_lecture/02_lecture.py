"""
함수 solution의 
첫번째 인자로는 dict_repr가 
두번째 인자로 문자열 key가 
세번째 인자로 정수 cut가 주어집니다.
ex. solution(dict_repr, 'Math', 70)

dict_repr은, 사람의 이름 (문자열) 을 키로 하고, 
그 사람의 세 과목 성적을 담은 사전을 값으로 하는 사전에 대한 문자열 표현입니다. 
예를 들면, 세 명의 학생 (Mary, Peter, John) 의 성적은 아래와 같은 형태의 문자열로 표현됩니다 
(읽기 편의상 삽입한 줄바꿈은 무시합니다).

문제에서는 학생들과 점수는 달라질 수 있지만, 항상 위와 같은 형태로 올바르게 해석될 수 있는 
사전을 표현한 문자열만이 주어진다고 가정합니다.

특정 과목의 점수가 일정 수준 이상인 학생들만을 골라 그 이름을 알파벳 순서로 정렬한 리스트 
(문자열들로 이루어진) 를 반환하는 함수 solution 을 완성하세요. 예를 들어, 위와 같은 성적표에서
key = "Math"`, `cut = 70 이 주어지는 경우의 올바른 리턴 값은
["John", "Peter"] 입니다. (수학 점수가 70 점 이상인 학생 두 명의 이름을 알파벳 순서로 정렬한 것)

다른 예로는, key = "Korean", cut = 70 이 주어지는 경우의 올바른 리턴 값은
["John", "Mary"] 입니다. (국어 점수가 70 점 이상인 학생 두 명의 이름을 알파벳 순서로 정렬한 것)
"""



dict_repr = {
    'Mary': {'Korean': 80, 'Math': 65, 'English': 58},
    'Peter': {'Korean': 60, 'Math': 95, 'English': 72},
    'John': {'Korean': 70, 'Math': 78, 'English': 69}
    }


def solution(dicts, key, cut):
    result = []
    for keys, values in dicts.items():
        if values.get(key) >= cut:
            result.append(keys)
    return sorted(result)


print(solution(dict_repr, 'Korean', 70))
print(solution(dict_repr, 'Math', 70))

