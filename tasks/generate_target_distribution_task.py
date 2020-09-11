from zquantum.qcbm.target import get_bars_and_stripes_target_distribution
from zquantum.core.bitstring_distribution import save_bitstring_distribution

def generate_bars_and_stripes_target_distribution(nrows, ncols, fraction, method):
    distribution = get_bars_and_stripes_target_distribution(nrows, ncols, fraction, method)

    save_bitstring_distribution(distribution, "distribution.json")