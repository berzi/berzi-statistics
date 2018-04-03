import main
import sys
import inspect


def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]


def test_that(dataset, tests: dict):
    for call, expected in tests.items():
        if not getattr(dataset, call)() == expected:
            print("TEST FAILED on data set:\n\t\t" + retrieve_name(dataset)[0] +
                  "\nSet:\t\t" + str(dataset.data()) +
                  "\nTest:\t\t" + call +
                  "\nOutput:\t\t" + str(getattr(dataset, call)()) +
                  "\nExpected:\t" + str(expected))
            sys.exit()


test_set1 = main.Dataset(1, 2, 3, 4)
test_that(test_set1, {
    "mean": 2.5,
    "median": 2.5,
    "q1": 1.5,
    "q3": 3.5,
    "iqr": 2,
    "mode": [],
    "range": 3,
    "mid_range": 2.5,
    "variance": 1.25,
    "standard_deviation": 1.1180339887498948482045868343656,
    "sample_variance": 1.6666666666666667,
    "sample_standard_deviation": 1.2909944487358056,
    "mad": 1,
    "is_skewed": 0,
})


test_set2 = main.Dataset(1, 2, 3, 4, 5, 6)
test_that(test_set2, {
    "mean": 3.5,
    "median": 3.5,
    "q1": 2,
    "q3": 5,
    "iqr": 3,
    "mode": [],
    "range": 5,
    "mid_range": 3.5,
    "variance": 2 + 11/12,
    "standard_deviation": 1.7078251276599330638701731134202,
    "sample_variance": 3.5,
    "sample_standard_deviation": 1.8708286933869707,
    "mad": 1.5,
    "is_skewed": 0,
})


test_set3 = main.Dataset(1, 2, 3, 4, 5, 6, 7)
test_that(test_set3, {
    "mean": 4,
    "median": 4,
    "q1": 2,
    "q3": 6,
    "iqr": 4,
    "mode": [],
    "range": 6,
    "mid_range": 4,
    "variance": 4,
    "standard_deviation": 2,
    "sample_variance": 4 + 2/3,
    "sample_standard_deviation": 2.160246899469287,
    "mad": 1.7142857142857142,
    "is_skewed": 0,
})


test_set4 = main.Dataset(1, 2, 3, 4, 5, 6, 7, 8, 9)
test_that(test_set4, {
    "mean": 5,
    "median": 5,
    "q1": 2.5,
    "q3": 7.5,
    "iqr": 5,
    "mode": [],
    "range": 8,
    "mid_range": 5,
    "variance": 6 + 2/3,
    "standard_deviation": 2.5819888974716112567861769331883,
    "sample_variance": 7.5,
    "sample_standard_deviation": 2.7386127875258306,
    "mad": 2 + 2/9,
    "is_skewed": 0,
})


test_set5 = main.Dataset(25, 87, 51, 97, 13, 48, 97, 13, 13)
test_that(test_set5, {
    "mean": 49 + 1/3,
    "median": 48,
    "q1": 13,
    "q3": 92,
    "iqr": 79,
    "mode": [13],
    "range": 84,
    "mid_range": 55,
    "variance": 1168 + 8/9,
    "standard_deviation": 34.189017079888226714835938705811,
    "sample_variance": 1315,
    "sample_standard_deviation": 36.26292872893749,
    "mad": 29.925925925925924,
    "is_skewed": 1,
})


test_set6 = main.Dataset(42, 58, 98, 89, 89, 22, 68, 88, 49, 60)
test_that(test_set6, {
    "mean": 66.3,
    "median": 64,
    "q1": 49,
    "q3": 89,
    "iqr": 40,
    "mode": [89],
    "range": 76,
    "mid_range": 60,
    "variance": 547.01,
    "standard_deviation": 23.388244910638335454722936879132,
    "sample_variance": 607 + 71/90,
    "sample_standard_deviation": 24.6533747971528,
    "mad": 20.1,
    "is_skewed": 1,
})


test_set7 = main.Dataset(42, 58, 98, 89, 89, 22, 88, 88, 49, 60)
test_that(test_set7, {
    "mean": 68.3,
    "median": 74,
    "q1": 49,
    "q3": 89,
    "iqr": 40,
    "mode": [89, 88],
    "range": 76,
    "mid_range": 60,
    "variance": 589.8100000000001,
    "standard_deviation": 24.286004199950227711811017530816,
    "sample_variance": 655 + 31/90,
    "sample_standard_deviation": 25.599696178752676,
    "mad": 22.1,
    "is_skewed": -1,
})


test_set8 = main.Dataset(1, 2, 1, 2, 3)
test_that(test_set8, {
    "mean": 1.8,
    "median": 2,
    "q1": 1,
    "q3": 2.5,
    "iqr": 1.5,
    "mode": [1, 2],
    "range": 2,
    "mid_range": 2,
    "variance": 0.56,
    "standard_deviation": 0.74833147735478827711674974646331,
    "sample_variance": 0.7000000000000001,
    "sample_standard_deviation": 0.8366600265340756,
    "mad": 0.64,
    "is_skewed": -1,
})


test_set9 = main.Dataset(1, 2, 1, 2)
test_that(test_set9, {
    "mean": 1.5,
    "median": 1.5,
    "q1": 1,
    "q3": 2,
    "iqr": 1,
    "mode": [],
    "range": 1,
    "mid_range": 1.5,
    "variance": 0.25,
    "standard_deviation": 0.5,
    "sample_variance": 1/3,
    "sample_standard_deviation": 0.5773502691896257,
    "mad": 0.5,
    "is_skewed": 0,
})


print("All tests successful!")
