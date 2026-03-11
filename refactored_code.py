
class ComputeStatistics:

    def __init__(self, data: list):
        self.data = data

    @classmethod
    def from_file(cls, filepath: str) -> "ComputeStatistics":
        data = cls._read_integers(filepath)
        return cls(data)

    @staticmethod
    def _read_integers(filepath: str) -> list:
        data = []
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    data.append(int(line))
        return data

    def count(self) -> int:
        return len(self.data)

    def summation(self) -> int:
        return sum(self.data)

    def average(self) -> float:
        return self.summation() / self.count()

    def minimum(self) -> int:
        return min(self.data)

    def maximum(self) -> int:
        return max(self.data)

    def display_stats(self):
        print("The values are:", self.data)
        print("Total values in data are:", self.count())
        print("Summation of data is:", self.summation())
        print("Average of data is:", round(self.average(), 2))
        print("Minimum value from data is:", self.minimum())
        print("Maximum value from data is:", self.maximum())


# Unit Tests

def test_count():
    cs = ComputeStatistics([15, 3, 42, 8, 27])
    assert cs.count() == 5, "count() failed"
    print("test_count passed")

def test_summation():
    cs = ComputeStatistics([15, 3, 42, 8, 27])
    assert cs.summation() == 95, "summation() failed"
    print("test_summation passed")

def test_average():
    cs = ComputeStatistics([10, 20, 30])
    assert cs.average() == 20.0, "average() failed"
    print("test_average passed")

def test_minimum():
    cs = ComputeStatistics([15, 3, 42, 8, 27])
    assert cs.minimum() == 3, "minimum() failed"
    print("test_minimum passed")

def test_maximum():
    cs = ComputeStatistics([15, 3, 42, 8, 27])
    assert cs.maximum() == 42, "maximum() failed"
    print("test_maximum passed")


if __name__ == "__main__":
    # Run tests
    print("=== Running Unit Tests ===")
    test_count()
    test_summation()
    test_average()
    test_minimum()
    test_maximum()
    print()

    print("=== Demo Output ===")
    sample_data = [15, 3, 42, 8, 27, 56, 11, 34, 19, 7]
    cs = ComputeStatistics(sample_data)
    cs.display_stats()
