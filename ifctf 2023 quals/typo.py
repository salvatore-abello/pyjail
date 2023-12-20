#!/usr/bin/env python3

import os
import subprocess
from abc import ABC

from Crypto.PublicKey import RSA


class SecureExecutor(ABC):
    def __init_subclass__(cls, interpeter: str):
        cls.interpeter = interpeter
        return super().__init_subclass__()

    def __init__(self, script: str, key: str):
        self.script = script
        self.key = key

    def get_encrypted_output(self) -> bytes:
        with open(self.key, "rb") as f:
            key = RSA.import_key(f.read())
        output = subprocess.check_output([self.interpeter, self.script], timeout=1, stdin=subprocess.DEVNULL)
        enc = pow(int.from_bytes(output, "big"), key.e, key.n)
        return enc.to_bytes(key.size_in_bytes(), "big")


class PythonExecutor(SecureExecutor, interpeter="python3"):
    pass


def main():

    try:
        print("Send me your script: ")
        script = bytes.fromhex(input())
        print("Send me your public key: ")
        key = bytes.fromhex(input())

        s_file = f"/tmp/{os.urandom(8).hex()}"
        k_file = f"/tmp/{os.urandom(8).hex()}"

        with open(s_file, "wb") as f:
            f.write(script)

        with open(k_file, "wb") as f:
            f.write(key)

        executor = PythonExecutor(s_file, s_file)
        print("Here is your encrypted output: ")
        print(executor.get_encrypted_output().hex())
    except Exception as e:
        print("An error occured")

if __name__ == "__main__":
    main()
