def appearance(intervals: dict[str, list[int]]) -> int:
    lesson = intervals['lesson']

    pupil = []
    for i in range(1, len(intervals['pupil']), 2):
        res = search_overlap([intervals['pupil'][i-1], intervals['pupil'][i]], lesson)
        if range(res[0], res[1]):
            pupil.append(res[0])
            pupil.append(res[1])

    tutor = []
    for i in range(1, len(intervals['tutor']), 2):
        res = search_overlap([intervals['tutor'][i - 1], intervals['tutor'][i]], lesson)
        if range(res[0], res[1]):
            tutor.append(res[0])
            tutor.append(res[1])

    sum_ = []
    for i in range(1, len(pupil), 2):
        for j in range(1, len(tutor), 2):
            res = search_overlap([pupil[i - 1], pupil[i]], [tutor[j - 1], tutor[j]])
            if range(res[0], res[1]):
                sum_ += list(range(res[0], res[1]))

    print(len(set(sum_)))
    return len(set(sum_))


def search_overlap(range1, range2):
    return max(range1[0], range2[0]), min(range1[1], range2[1])


tests = [
    {'intervals': {'lesson': [1894663200, 1894666800],
             'pupil': [1894663340, 1894663389, 1894663390, 1894663395, 1894663396, 1894666472],
             'tutor': [1894663290, 1894663430, 1994663443, 1994666473]},
     'answer': 88
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
