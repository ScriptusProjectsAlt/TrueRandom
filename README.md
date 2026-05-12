<div align="center">

# TrueR

### Advanced True Random Number Generation for Python

<br>

<img src="https://img.shields.io/badge/python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/status-stable-2ea043?style=for-the-badge&logo=github">
<img src="https://img.shields.io/badge/randomness-entropy_based-ff6b35?style=for-the-badge&logo=cloudflare">
<img src="https://img.shields.io/badge/license-MIT-8b5cf6?style=for-the-badge&logo=open-source-initiative&logoColor=white">

<br><br>

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="90">

<br>

**TrueR** is a modern Python package focused on generating  
high-quality entropy-based random numbers instead of relying solely  
on predictable pseudo-random generation algorithms.

Fast • Lightweight • Entropy Powered

</div>

---

# <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="22"> Features

- Entropy-based randomness
- Lightweight and fast
- Simple and clean API
- Modern Python support
- Better unpredictability than standard PRNG systems
- Suitable for simulations and security tooling

---

# <img src="https://cdn-icons-png.flaticon.com/512/906/906334.png" width="22"> Installation

Proper Install:
```bash
pip install git+https://github.com/ScriptusProjectsAlt/TrueRandom.git
```


Install from source:

```bash
git clone https://github.com/ScriptusProjectsAlt/TrueRandom
cd TrueRandom
pip install .
```

Or install in development mode:

```bash
pip install -e .
```

---

# <img src="https://cdn-icons-png.flaticon.com/512/1828/1828919.png" width="22"> Quick Example

```python
from truer import TrueR

rng = TrueR()

print(rng.randint(1, 100))  # Random integer: 42
print(rng.random())          # Random float: 0.123456789
print(rng.randbytes(8))      # Random bytes: b'\x01\x23\x45\x67\x89\xab\xcd\xef'
```

---

# <img src="https://cdn-icons-png.flaticon.com/512/1828/1828884.png" width="22"> Usage

## Basic Usage

```python
from truer import TrueR

# Create an RNG instance
rng = TrueR()

# Generate a random integer between 1 and 100
random_int = rng.randint(1, 100)

# Generate a random float between 0.0 and 1.0
random_float = rng.random()

# Generate 16 random bytes
random_bytes = rng.randbytes(16)
```

## Configuration Options

```python
# Use only OS entropy (disable CPU jitter for faster generation)
rng = TrueR(use_cpu_jitter=False)

# Default behavior (uses both OS entropy and CPU jitter)
rng = TrueR(use_cpu_jitter=True)  # or simply TrueR()
```

## Integration Examples

```python
# Simulate a dice roll
dice_roll = rng.randint(1, 6)

# Generate random bytes for cryptographic use
key = rng.randbytes(32)  # 256-bit key

# Generate a random float for probability simulations
probability = rng.random()
```

---

# <img src="https://cdn-icons-png.flaticon.com/512/2721/2721297.png" width="22"> Examples

## Random Integer

```python
from truer import TrueR

rng = TrueR()

number = rng.randint(1, 999999)
print(number)  # e.g., 123456
```

## Random Float

```python
value = rng.random()
print(value)  # e.g., 0.987654321
```

## Random Bytes

```python
bytes_data = rng.randbytes(16)
print(bytes_data)  # e.g., b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
```

## Disable CPU Jitter (Optional)

```python
rng = TrueR(use_cpu_jitter=False)  # Uses only OS entropy
```

---

# <img src="https://cdn-icons-png.flaticon.com/512/1006/1006771.png" width="22"> How It Works

Traditional random libraries rely on  
**Pseudo-Random Number Generators (PRNGs)**.

PRNG systems are deterministic:
- Same seed → same output
- Outputs can become predictable

**TrueR** gathers entropy from system-level sources to improve unpredictability and generate stronger random values.

---

# <img src="https://cdn-icons-png.flaticon.com/512/1828/1828884.png" width="22"> Benchmark

| Generator | Predictable | Entropy Based | Security Friendly |
|-----------|-------------|----------------|-------------------|
| `random`  | Yes | No | No |
| `TrueR`   | Minimal | Yes | Better |

---

# <img src="https://cdn-icons-png.flaticon.com/512/3767/3767084.png" width="22"> Project Structure

```
truer/
│
├── truer/
│   ├── __init__.py
│   ├── core/
│   │   ├── engine.py
│   │   └── rng.py
│   ├── entropy/
│   │   ├── base.py
│   │   ├── cpu_jitter.py
│   │   ├── mixer.py
│   │   ├── microphone.py
│   │   └── os_entropy.py
│   └── utils/
│       ├── conversation.py
│       └── validation.py
│
├── examples/
│   ├── basic_usage.py
│   ├── demo.py
│   └── entropy_mix.py
├── tests/
│   └── test_rng.py
├── pyproject.toml
├── README.md
└── LICENSE
```

---

# <img src="https://cdn-icons-png.flaticon.com/512/3524/3524659.png" width="22"> Development

Clone the repository:

```bash
git clone https://github.com/ScriptusProjectsAlt/TrueRandom
```

Install in development mode:

```bash
pip install -e .
```

Run tests:

```bash
python -m pytest tests/
```

Or run a specific test:

```bash
python -c "from tests.test_rng import test_randint; test_randint(); print('Test passed')"
```

---

# <img src="https://cdn-icons-png.flaticon.com/512/942/942748.png" width="22"> Roadmap

- [ ] Hardware entropy support
- [ ] Quantum randomness integration
- [ ] Random byte streams
- [ ] Cryptographic utilities
- [ ] Async entropy collection

---

# <img src="https://cdn-icons-png.flaticon.com/512/1077/1077046.png" width="22"> Contributing

Contributions are welcome.

To contribute:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

# <img src="https://cdn-icons-png.flaticon.com/512/942/942799.png" width="22"> License

Released under the MIT License.

---

<div align="center">

## Support The Project

If you like **TrueR**, consider starring the repository.

<br>

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="40">

</div>
