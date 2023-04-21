# Cockroach


def cockroach_speed(speed_km_per_hour):
    speed_cm_per_second = int(speed_km_per_hour * 1000 * 100 / (60 * 60))
    return speed_cm_per_second


def assert_equals(a, b):
    print(a == b)


assert_equals(cockroach_speed(1.08),30)
assert_equals(cockroach_speed(1.09),30)
assert_equals(cockroach_speed(0),0)
