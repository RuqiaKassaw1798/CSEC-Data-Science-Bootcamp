import math

class StatEngine:
    def __init__(self, data):
        if not data:
            raise ZeroDivisionError("Dataset cannot be empty.")
        self.data = self._clean(data)

    def _clean(self, data):
        cleaned = []
        for x in data:
            if isinstance(x, (int, float)):
                cleaned.append(float(x))
            else:
                raise TypeError(f"Invalid type: {type(x)}. Expected int or float.")
        return cleaned

    def get_mean(self):
        return sum(self.data) / len(self.data)

    def get_median(self):
        d = sorted(self.data)
        n = len(d)
        mid = n // 2
        if n % 2 == 0:
            return (d[mid - 1] + d[mid]) / 2
        return d[mid]

    def get_mode(self):
        counts = {}
        for x in self.data:
            counts[x] = counts.get(x, 0) + 1
        max_freq = max(counts.values())
        if max_freq == 1 and len(self.data) > 1:
            return "All values are unique."
        return [k for k, v in counts.items() if v == max_freq]

    def get_variance(self, is_sample=True):
        n = len(self.data)
        mean_val = self.get_mean()
        total_sq_diff = 0
        mean_val = self.get_mean()
        for val in self.data:
            diff = val - mean_val
            total_sq_diff += diff ** 2
        if is_sample:
            return total_sq_diff / (n - 1)
        else:
            return total_sq_diff / n

    def get_std_dev(self, is_sample=True):
        return math.sqrt(self.get_variance(is_sample))

    def get_outliers(self, threshold=2):
        mean_val = self.get_mean()
        sd = self.get_std_dev(is_sample=True)
        return [x for x in self.data if abs(x - mean_val) > (threshold * sd)]