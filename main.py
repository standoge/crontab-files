from functions import recollect, snapshot

def main():

    try:
        recollect()
    except:
        print("Something was wrong to start, check recollect function")
    finally:
        snapshot()

if __name__ == '__main__':
    main()
