from functions import filter, count


def main():

    try:
        filter()
    except Exception as e:
        print("Something was wrong to start, check recollect function")
        print(e)
    finally:
        count()


if __name__ == "__main__":
    main()
