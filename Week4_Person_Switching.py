
Personas={
    "default": {
        "name": "Default Persona",
        "prompt": "You are a helpful assistant,which gives precise answers."
    },
    "coder": {
        "name": "Coder Persona",
        "prompt": "You are a skilled programmer who can write code in various languages."
    },
    "teacher": {
        "name": "Teacher Persona",
        "prompt": "You are an experienced teacher who can explain complex concepts in simple terms."
    },
}


current_persona = "coder"

Personas = Personas[current_persona]

history[0] = {"role": "system", "content": Personas["prompt"]}

def apply_sliding_window(history, max_turns=10):
    system_message = history[0]
    conversation_history = history[1:]
    max_messages = max_turns * 2
    
    if len(conversation_history) <= max_messages:
        return history
    trimmed_history = conversation_history[-max_messages:]
    return [system_message] + trimmed_history
    