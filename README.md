# Discrete Logarithm

## Overview

This repository provides implementations of several algorithms to compute the **discrete logarithm**, a concept crucial in mathematics and cryptography.

In mathematics, for given real numbers \( a \) and \( b \), the logarithm \( \log_b(a) \) is a number \( x \) such that \( b^x = a \). Similarly, in any group \( G \), powers \( b^k \) can be defined for all integers \( k \), and the **discrete logarithm** \( \log_b(a) \) is an integer \( k \) such that \( b^k = a \).

Discrete logarithms play a significant role in cryptography. The security of many encryption systems relies on the computational difficulty of finding a discrete logarithm. If a "fast" (linear-time) algorithm were discovered, it would undermine the security of these systems, necessitating their redesign.

---

## Features

This repository includes:
- Implementations of various methods to compute the discrete logarithm of an element in \( \mathbb{Z}/(p\mathbb{Z})^* \), where \( p \) is a prime number.
- Supported algorithms:
  - **Brute Force**
  - **Baby-Step Giant-Step**
  - **Pohlig-Hellman Reduction**
- A utility to compare the efficiency of these algorithms using the `measure` function.

---

## Usage

Clone the repository and explore the implementations provided. The algorithms are designed to help you understand and experiment with the discrete logarithm problem in modular arithmetic.

---

## Contribution

Contributions to improve the repository, optimize algorithms, or expand functionality are welcome. Feel free to submit issues or pull requests.
