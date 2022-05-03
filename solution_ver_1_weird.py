from fractions import Fraction
test_1 = [1, 51]
test_2 = [4, 30, 50]
test_3 = [4, 17, 50]
test_4 = [25, 105, 145, 170]
test_5 = [1, 9, 10, 12]
test_6 = [2, 10, 11, 13]


def solution(the_list):
    distance_list = get_distance_for_every_two_pegs(the_list)
    # The sum is the first and list gear relationship, it's either G1 + Gn(for even list), or G1 - Gn(for odd list)
    distance_sum = get_alternating_sum(distance_list)
    # Rules:
    #     1. The first gear must be greater than the last gear, and they are all positive integers
    #     2. It's impossible for G1 + Gn or G1 - Gn to be less than 1
    #     3. The ratio has to be greater than 1
    #     4. The smallest gear size is 1
    if distance_sum <= 0:
        return [-1, -1]
    if list_is_even(the_list):
        # In this case 3Gn = distance_sum
        # Making sure the last gear is greater than 1
        # So the first one is also greater than 1
        if (distance_sum / 3) < 1:
            return [-1, -1]
        if distance_sum % 3 == 0:
            first_gear = (distance_sum / 3) * 2
            return [first_gear, 1]
        return check_for_each_gear_size(Fraction(distance_sum * 2, 3), distance_list)

    one_last_gear_radius = distance_sum
    first_gear = 2 * one_last_gear_radius

    return check_for_each_gear_size(Fraction(first_gear), distance_list)


def list_is_even(the_list):
    """
    Returns True if given list is even size; otherwise returns False
    """
    return len(the_list) % 2 == 0


def get_distance_for_every_two_pegs(the_list):
    """
    Given a list of integers, returns a list of list[i + 1] - list[i]
    """
    list_range = [i for i in range(len(the_list) - 1)]
    return list(map(lambda i: the_list[i + 1] - the_list[i], list_range))


def get_alternating_sum(distance_list):
    """
    Given a list of real numbers, returns list[i] + (- list[i+1]) + list[i+2] + .....
    """
    distance_alternating_sum = 0
    toggle = 1
    for distance in distance_list:
        distance_alternating_sum += (distance * toggle)
        toggle *= -1

    return distance_alternating_sum


def check_for_each_gear_size(first_gear, distance_list):
    """
    Given the radius of the first gear, and the distance list, deduct the radius of every gear
    If there's a radius less than 1, returns True; otherwise returns False
    """
    checking_gear = first_gear
    for distance in distance_list:
        checking_gear = distance - checking_gear
        if checking_gear < 1:
            return [-1, -1]

    return [first_gear.numerator, first_gear.denominator]


print(solution(test_1))
print(solution(test_2))
print(solution(test_3))
print(solution(test_4))
print(solution(test_5))
print(solution(test_6))
