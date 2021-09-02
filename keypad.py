def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12

    for number in numbers:
        if number == 0:
            number = 11
        if number == 1 or number == 4 or number == 7:
            answer += 'L'
            left = number
        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            right = number
        else:
            print(left, right, number)
            if(int(abs(number - left) / 3) + abs(number - left) % 3 == int(abs(number - right) / 3) + abs(number - right) % 3):
                if hand == 'left':
                    answer += 'L'
                    left = number
                else:
                    answer += 'R'
                    right = number
            elif(int(abs(number - left) / 3) + abs(number - left) % 3 > int(abs(number - right) / 3) + abs(number - right) % 3):
                answer += 'R'
                right = number
            elif(int(abs(number - left) / 3) + abs(number - left) % 3 < int(abs(number - right) / 3) + abs(number - right) % 3):
                answer += 'L'
                left = number

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
