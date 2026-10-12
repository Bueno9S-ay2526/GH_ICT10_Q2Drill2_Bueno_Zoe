# checking members
from pyscript import display, document


def check_members (e):
    last_name = document.getElementById('surname').value.title().strip()
    first_name = document.getElementById('first_name').value.title().strip()
    full_name = last_name + ', ' + first_name
    members_list = ['Lopido, Marti', 'Santos, Joshua', 'Pasco, Kristine', 'Ortiz, Josua', 'Me, I']
    member_checker = full_name in members_list

    display_message = (f'Sorry {full_name}, your name is not on the list.', f'Congratulations {full_name}! You are now part of the ICT club.')
    display(display_message[member_checker], target='result_box', append=False)