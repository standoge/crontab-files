from functions import filter, snapshot


def main():

    try:
        filter()
    except:
        print("Something was wrong to start, check recollect function")
    finally:
        snapshot()


if __name__ == "__main__":
    main()
