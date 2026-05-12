import struct
from ..entropy import os_entropy, cpu_jitter, mixer


class TrueR:
    def __init__(self, use_cpu_jitter: bool = True):
        self.use_cpu_jitter = use_cpu_jitter

    def _get_entropy(self) -> bytes:
        sources = [os_entropy.get_entropy()]
        if self.use_cpu_jitter:
            sources.append(cpu_jitter.get_entropy())
        return mixer.mix(*sources)

    def randbytes(self, n: int) -> bytes:
        if n <= 0:
            return b""
        result = b""
        while len(result) < n:
            entropy = self._get_entropy()
            result += entropy
        return result[:n]

    def random(self) -> float:
        entropy = self._get_entropy()
        val = struct.unpack('>Q', entropy[:8])[0]
        return val / (1 << 64)

    def randint(self, a: int, b: int) -> int:
        if a > b:
            raise ValueError("a must be <= b")
        range_size = b - a + 1
        if range_size <= 0:
            raise ValueError("range is empty")
        num_bytes = (range_size.bit_length() + 7) // 8
        max_val = 1 << (num_bytes * 8)
        while True:
            entropy = self._get_entropy()
            val = int.from_bytes(entropy[:num_bytes], 'big')
            if val < max_val - (max_val % range_size):
                return a + (val % range_size)
    ...