import base64 as b64
from dataclasses import dataclass

@dataclass
class row():
    k: str
    v: str

    def decode(self):
        return b64.b64decode(self.v).decode()

    def encode(self):
        return b64.b64encode(self.v.encode())

    def __str__(self):
        return f"{self.k}: {self.encode().decode()}"

@dataclass
class secret():
    rows: list

    def add(self, k, v):
        self.rows.append(row(k, v))

    def load(self):
        pass

    def secret_header(self, secret_name: str, namespace: str):
        return f"""apiVersion: v1
kind: Secret
metadata:
  name: {secret_name}
  namespace: {namespace}
type: Opaque
data:
"""

    def print_secret(self, secret_name: str, namespace: str):
        print(self.secret_header(secret_name, namespace))
        for i in self.rows:
            print(f"  {i}")


if __name__ == "__main__":
    s = secret([])
    s.add("test", "valore")
    s.add("k2", "valore2")
    # print(s)

    s.print_secret('secretname', 'myns')
