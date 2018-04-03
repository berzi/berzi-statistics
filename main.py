import collections
import math


class Dataset(object):
    """A set of data points."""
    def __init__(self, *args):
        """Accepts a list of numbers as data."""
        self.__data = [arg for arg in args]

        # Create dictionaries to cache results to improve performance if values are requested multiple times.
        self.__central_tendency = dict()
        self.__spread = dict()

    def data(self):
        """Return the data set."""
        return self.__data

    def sorted_data(self):
        """Return the data set, sorted."""
        return sorted(self.__data)

    def mean(self):
        """Calculate the population mean µ of the data set."""
        if "mean" not in self.__central_tendency:
            # Sum the data points together and divide by the amount of data points.
            self.__central_tendency["mean"] = sum(self.__data) / len(self.__data)

        return self.__central_tendency["mean"]

    def median(self):
        """Calculate the median of the dataset."""
        if "median" not in self.__central_tendency:
            dataset = self.sorted_data()  # Sort the data in ascending order.
            length = len(dataset)
            # The median entry is located in the middle of the collection. We subtract 1 to account for 0-index.
            median_index = -(-length // 2)-1

            if length % 2 == 0:
                # If the collection has an even number of items, the median is the mean of the two middle points.
                self.__central_tendency["median"] = (dataset[median_index]+dataset[median_index+1]) / 2
            else:
                # Otherwise it's exactly the middle point.
                self.__central_tendency["median"] = dataset[median_index]

        return self.__central_tendency["median"]

    def mode(self):
        """Find the data points occurring most often.

        :return: a list of most occurring numbers or an empty list if no mode is present.
        """

        counter = collections.Counter(self.__data)  # Count how many times each discrete number occurs.

        top_occurrence = None
        most_occurring = []
        for item, occurrences in counter.most_common():
            if top_occurrence is None or occurrences > top_occurrence:
                # If we don't have a most occurring number yet or the current item's occurrences are higher,
                # store the new ones.
                most_occurring = [item]
                top_occurrence = occurrences
            elif occurrences == top_occurrence:
                # If the item we're iterating on has the same number of occurrences as our top item(s), add it to them.
                most_occurring.append(item)

        if set(most_occurring) == set(self.__data):
            # If our set of most occurring items equals our whole data set, there is no mode.
            return []

        return most_occurring

    def q1(self):
        """Calculate the median of the first quarter of the data."""
        if "q1" not in self.__central_tendency:
            dataset = self.sorted_data()
            top_length = len(dataset)  # Get the length and index of the median value of our main data set.
            top_median_index = -(-top_length // 2)

            # Split the dataset picking the first half.
            if top_length % 2 == 0:
                first_half = dataset[:top_median_index]
            else:
                # If our main data set has an odd number of elements, count one index to the left to exclude the median.
                first_half = dataset[:top_median_index-1]

            # Get the same metrics as above for our subset.
            length = len(first_half)
            bottom_median_index = -(-length//2)-1

            # Get the median of the subset.
            if length % 2 == 0:
                self.__central_tendency["q1"] = (first_half[bottom_median_index] + first_half[bottom_median_index+1])/2
            else:
                self.__central_tendency["q1"] = first_half[bottom_median_index]

        return self.__central_tendency["q1"]

    def q3(self):
        """Calculate the median of the third quarter of the data."""
        if "q3" not in self.__central_tendency:
            dataset = self.sorted_data()
            top_median_index = -(-len(dataset)//2)

            # Split the dataset and pick the second half.
            # Since the median index is calculated rounding up, we don't need to check if the set is even or odd.
            first_half = dataset[top_median_index:]
            length = len(first_half)
            bottom_median_index = -(-length//2)-1

            if length % 2 == 0:
                self.__central_tendency["q3"] = (first_half[bottom_median_index] + first_half[bottom_median_index+1])/2
            else:
                self.__central_tendency["q3"] = first_half[bottom_median_index]

        return self.__central_tendency["q3"]

    def iqr(self):
        """Calculate the interquartile range of the data."""
        if "iqr" not in self.__central_tendency:
            # The interquartile range equals the third quarter's median minus the first one's.
            self.__central_tendency["iqr"] = self.q3()-self.q1()

        return self.__central_tendency["iqr"]

    def range(self):
        """Calculate the range of the data set."""
        if "range" not in self.__spread:
            # The range equals the highest number minus the smallest number of the data set.
            self.__spread["range"] = max(self.__data) - min(self.__data)

        return self.__spread["range"]

    def variance(self):
        """Calculate the population variance σ² of the data set."""
        if "variance" not in self.__spread:
            sum_of_square_differences = 0
            for value in self.__data:
                # Sum together the squared difference of each data point from the mean.
                difference_from_mean = value - self.mean()
                sum_of_square_differences += difference_from_mean**2

            # Divide by the number of data points to get the variance.
            self.__spread["variance"] = sum_of_square_differences / len(self.__data)

        return self.__spread["variance"]

    def standard_deviation(self):
        """Calculate the population variance σ of the data set."""
        if "standard deviation" not in self.__spread:
            # Standard deviation equals the square root of the variance.
            self.__spread["standard deviation"] = math.sqrt(self.variance())

        return self.__spread["standard deviation"]

    def sample_variance(self):
        """Calculate the unbiased sample variance s² of the data set as the sample of a population."""
        if "sample variance" not in self.__spread:
            # The sample variance is similar to the population variance but we divide by the number of data points...
            # ...minus one to reduce the bias given from the sample not being representative of the whole population.
            sum_of_square_differences = 0
            for value in self.__data:
                difference_from_mean = value - self.mean()
                sum_of_square_differences += difference_from_mean**2

            self.__spread["sample variance"] = sum_of_square_differences / (len(self.__data)-1)

        return self.__spread["sample variance"]

    def sample_standard_deviation(self):
        """Calculate the sample standard deviation s of the data set as the sample of a population."""
        if "sample standard deviation" not in self.__spread:
            # The standard deviation of a sample of the population is the square root of the sample variance.
            self.__spread["sample standard deviation"] = math.sqrt(self.sample_variance())

        return self.__spread["sample standard deviation"]
