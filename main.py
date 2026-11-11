from bakery import assert_equal
from drafter import *
from dataclasses import dataclass



hide_debug_information()
set_website_title("Your Drafter Website")
set_website_framed(False)


@dataclass
class State:
    pass


@route
def index(state: State) -> Page:
    return Page(state, ["Hello CS1!"])

assert_equal(index(State()), Page(State(), ["Hello CS1!"]))

start_server(State())
