from functions import recollect, make_snapshots

def main():

    try:
        recollect()
    except:
        print("something was wrong to start")
    finally:
        make_snapshots()


if __name__ == '__main__':
    main()
