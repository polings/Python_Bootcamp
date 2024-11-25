from random import uniform
from time import sleep


def emit_gel(step):
    """
    Simulates the measured pressure of a liquid.
    Generates an infinite stream of numbers from 0 to 100 (values > 100 are considered an error)
    with a random step sampled from the range [0, step]
    """
    pressure = 50
    while True:
        increment = uniform(0, step)
        pressure += increment
        if pressure > 100:
            raise ValueError(f"Pressure is higher than 100: {round(pressure, 2)}")
        reverse_sign = yield pressure
        if reverse_sign is not None:
            step = -step


def valve(initial_step):
    """
    Monitors and controls liquid pressure using a generator.
    Starts with an initial step value and responds to specific pressure thresholds
    by either reversing direction or triggering an emergency stop.
    """
    gen = emit_gel(initial_step)
    pressure = next(gen)
    print(pressure)
    sleep(0.8)
    while True:
        if pressure < 10 or pressure > 90:
            print(f"Emergency break! Pressure is {round(pressure, 2)}.")
            gen.close()
            break
        elif pressure < 20 or pressure > 80:
            print('reverse')
            pressure = gen.send('reverse sign')
            print(pressure)
        elif 20 <= pressure <= 80:
            pressure = next(gen)
            print(pressure)
        sleep(0.8)


def main():
    valve(initial_step=20)


if __name__ == "__main__":
    main()
