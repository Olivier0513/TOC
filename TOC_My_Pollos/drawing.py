from fsm import TocMachine

machine = TocMachine(
    states=["user", "eat", 'drink',"big", "small", 'thank', 'show_fsm'],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "eat",
            "conditions": "is_going_to_eat",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "drink",
            "conditions": "is_going_to_drink",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "show_fsm",
            "conditions": "is_going_to_show_fsm",
        },
        {
            "trigger": "advance",
            "source": "eat", 
            "dest": "small",
            "conditions": "is_going_to_small",
        },
        {
            "trigger": "advance",
            "source": "eat", 
            "dest": "big",
            "conditions": "is_going_to_big",
        },
        {
            "trigger": "advance",
            "source": "small", 
            "dest": "thank",
            "conditions": "is_going_to_thank",
        },
        {
            "trigger": "advance",
            "source": "big", 
            "dest": "thank",
            "conditions": "is_going_to_thank",
        },
        {
            "trigger": "advance",
            "source": "drink", 
            "dest": "thank",
            "conditions": "is_going_to_thank",
        },
        {
            "trigger": "advance",
            "source": "thank", 
            "dest": "user",
            "conditions": "is_going_to_user",
        },
        {
            "trigger": "advance",
            "source": "show_fsm", 
            "dest": "user",
            "conditions": "is_going_to_user",
        },
        {"trigger": "go_back", "source": ["eat", "drink", "big", "small", 'thank', 'show_fsm'], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

machine.get_graph().draw("fsm.png", prog="dot", format="png")
