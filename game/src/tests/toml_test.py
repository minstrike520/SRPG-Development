import toml

def test():
    d = toml.read("mock_config.toml")

    print(d)