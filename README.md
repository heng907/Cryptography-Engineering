# Diffie-Hellman Key Exchange Algorithm

This Python script implements the Diffie-Hellman key exchange algorithm, a method for securely exchanging cryptographic keys over a public channel. The Diffie-Hellman algorithm allows two parties to generate a shared secret key that can be used for encrypted communication.

## Features

- Secure generation of private keys using Python's `secrets` module.
- Efficient modular exponentiation using Python's built-in `pow` function.
- Assertion to ensure both parties compute the same shared secret.

## Prerequisites

- Python 3.6 or higher.

## How to Use

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/diffie-hellman-key-exchange.git
    cd diffie-hellman-key-exchange
    ```

2. **Run the script:**

    ```sh
    python diffie_hellman.py
    ```

## Example

The script uses a small prime number \( p \) and a base \( g \) for demonstration purposes. In a real-world application, \( p \) should be a large prime number to ensure security.

```python
if __name__ == "__main__":
    # Example of a large prime number and a base
    p = 23  # A large prime number
    g = 5   # A primitive root modulo p
    
    shared_secret = diffie_hellman(p, g)
    print(f"Shared secret: {shared_secret}")
