# def silencer(func):
#
#     def wrapper(x):
#         choice = input("Choose a silencer: ")
#
#         gas_silencer = "****" + str(func).lower() + "****"
#         pillow = "pfff" + str(func).lower() + "fffp"
#
#         if choice == str(gas_silencer):
#             print(gas_silencer)
#         elif choice == str(pillow):
#             print(pillow)
#         else:
#             print(f"Well, I knew you're an amateur.\n {func}")
#         return wrapper
#
#
# @silencer
# def gun(sound: str) -> str:
#     return sound


def type_of_silencer(type = None):
    types = 'pillow', 'silencer', 'glass'
    while type not in types: type = input("Choose from the following:\n 'pillow', 'bottle', 'silencer'")

    def silencer(func):
        def wrapper():
            return f'silenced with {type} no {func()}'
        return wrapper
    return silencer

@type_of_silencer('silencer')
def shotgun():
    return 'BOOM'

print(shotgun())