def solution(my_string, num1, num2):
    str_list = list(my_string)
    tmp = str_list[num1]
    str_list[num1]=str_list[num2]
    str_list[num2]=tmp
    answer = ''.join(str_list)
    return answer