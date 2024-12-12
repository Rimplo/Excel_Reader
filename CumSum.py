class CumSum:
    def __init__(self, dataset):
        """
        Initialize a CumSum object with a dataset.
        :param dataset: List of numerical data.
        """
        self.dataset = dataset
        self.Mean = 0
        self.CumSum = []

    def get_mean(self):
        """
        Calculate the mean of the dataset.
        :return: Mean of the dataset.
        """
        if len(self.dataset) == 0:
            return 0
        total = sum(self.dataset)
        self.Mean = total / len(self.dataset)
        return self.Mean

    def get_cumsum(self):
        """
        Calculate the cumulative sum adjusted by the mean.
        :return: List of cumulative sums adjusted by the mean.
        """
        self.CumSum = []  # Initialize an empty list for cumulative sums
        avg = self.get_mean()
        cumulative = 0

        for value in self.dataset:
            cumulative += (value - avg)
            self.CumSum.append(cumulative)

        return self.CumSum
