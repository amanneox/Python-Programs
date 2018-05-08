def psycho():
    print("Please tell me your problem")
    while True:
        answer=yield
        if answer is not None:
            if answer.endswith('?'):
                print("Don't ask yourself too much questions")
            elif 'good' in answer:
                print("A that's good, go on")
            elif 'bad' in answer:
                print("Don't be so negitive")
free=psycho()
next(free)
free.send("I am bad")
