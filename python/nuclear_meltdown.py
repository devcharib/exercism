"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature >= 800 or neutrons_emitted <= 500:
        return False
    return temperature * neutrons_emitted < 500000


def reactor_efficiency(voltage, current, theoretical_max_power):
    percentage = int(((voltage * current) / theoretical_max_power) * 100)
    if percentage >= 80:
        return 'green'
    if percentage >= 60:
        return 'orange'
    if percentage >= 30:
        return 'red'
    return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    prod = int(temperature * neutrons_produced_per_second)
    print(prod)
    if prod < threshold * 0.9:
        return 'LOW'
    if prod <= threshold * 1.1:
        return 'NORMAL'
    return 'DANGER'

x = is_criticality_balanced(750,950)
print(x)