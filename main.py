from functions import filter, snapshot, count


def main():

    try:
        filter()
    except:
        print("Something was wrong to start, check recollect function")
    finally:
        snapshot()
        count()


if __name__ == "__main__":
    main()
