from functions import recollect, make_snapshots

def main():

    try:
        recollect()
    except:
        print("something was wrong to start, check recollect function")
    finally:
        make_snapshots()


if __name__ == '__main__':
    main()
