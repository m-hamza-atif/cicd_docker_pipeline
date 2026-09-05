def greet(name="cicd-docker-practice"):
    return f"Hello from {name}!"


def add(first_number, second_number):
    return first_number + second_number


def main():
    print(greet())


if __name__ == "__main__":
    main()
