import retrying

i = 1;

@retrying.retry(
    stop_max_attempt_number=5,
    retry_on_exception=lambda ex: True,
    wait_exponential_multiplier=500,
    wait_exponential_max=8000)
def foo():
    global i;
    print(f'Try foo...{i}')
    i+=1
    if i < 3:
        raise Error('Any error')

    print('Success')


foo()
