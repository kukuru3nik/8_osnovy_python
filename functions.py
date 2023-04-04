# ф-я проверки на число
def check_ans_num(question):
    answer = ''
    while not answer.isdigit():
        answer = input(f'{question}\n')
    return answer
