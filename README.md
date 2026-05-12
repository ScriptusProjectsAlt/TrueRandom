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

```bash
pip install truer
```

Or install manually:

```bash
git clone https://github.com/yourname/truer
cd truer
pip install .
```

---

# <img src="https://cdn-icons-png.flaticon.com/512/1828/1828919.png" width="22"> Quick Example

```python
from truer import TrueR

rng = TrueR()

print(rng.randint(1, 100))
print(rng.random())
print(rng.choice(["apple", "banana", "orange"]))
```

---

# <img src="https://cdn-icons-png.flaticon.com/512/2721/2721297.png" width="22"> Examples

## Random Integer

```python
from truer import TrueR

rng = TrueR()

number = rng.randint(1, 999999)
print(number)
```

## Random Float

```python
value = rng.random()
print(value)
```

## Random Choice

```python
items = ["red", "blue", "green"]

print(rng.choice(items))
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

```txt
truer/
│
├── truer/
│   ├── __init__.py
│   ├── core.py
│   └── entropy.py
│
├── tests/
├── README.md
├── pyproject.toml
└── LICENSE
```

---

# <img src="https://cdn-icons-png.flaticon.com/512/3524/3524659.png" width="22"> Development

Clone the repository:

```bash
git clone https://github.com/yourname/truer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest
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