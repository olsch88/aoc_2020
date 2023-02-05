if __name__ == "__main__":
    for i in range(1, 26):
        filename = "d" + str(i)
        try:
            exec("from " + filename + " import main")
        except ModuleNotFoundError:
            print(f"No Solution for day {i}")
        else:
            eval("main()")
        print()
