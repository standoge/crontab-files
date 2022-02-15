from functions import recollect, snapshot

def main():

    try:
        recollect()
    except:
        print("something was wrong to start, check recollect function")
    finally:
        snapshot()

if __name__ == '__main__':
    main()
