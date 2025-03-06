import random
import re
import time
from datetime import datetime

class RuleBasedChatbot:
    def __init__(self):
        # Dictionary of patterns and possible responses
        self.patterns = {
            # Greetings - improved pattern to catch variations
            r'\b(hi+|hello+|hey+|howdy|greetings|good morning)\b': [
                "Hello there! How can I help you today?",
                "Hi! Nice to chat with you. What's on your mind?",
                "Hey! How are you doing today?"
            ],
            
            # Farewell
            r'\b(bye|goodbye|exit|quit)\b': [
                "Goodbye! Have a nice day!",
                "Bye! Come back if you have more questions.",
                "See you later! Take care!"
            ],
            
            # About the bot
            r'\bname\b': [
                "My name is ChattyBot. Nice to meet you!",
                "I'm ChattyBot, your friendly neighborhood chatbot.",
                "You can call me ChattyBot!"
            ],
            
            # How are you
            r'\bhow are you\b|\bhow\'s it going\b': [
                "I'm just a computer program, but I'm functioning well. Thanks for asking!",
                "I'm doing great! How about you?",
                "All systems operational! Thanks for your concern."
            ],
            
            # Weather
            r'\bweather\b': [
                "I don't have access to real-time weather data, but I hope it's nice outside!",
                "I can't check the weather, but maybe look out your window?",
                "Weather forecasting isn't in my skill set, unfortunately."
            ],
            
            # Time
            r'\btime\b|\bwhat time\b': [
                f"The current time is {datetime.now().strftime('%H:%M:%S')}.",
                f"It's {datetime.now().strftime('%I:%M %p')} right now.",
                f"My clock shows {datetime.now().strftime('%H:%M')}."
            ],
            
            # Date
            r'\bdate\b|\btoday\b|\bday\b': [
                f"Today is {datetime.now().strftime('%A, %B %d, %Y')}.",
                f"It's {datetime.now().strftime('%d/%m/%Y')} today.",
                f"The date is {datetime.now().strftime('%B %d, %Y')}."
            ],
            
            # Thanks
            r'\bthank|\bthanks\b': [
                "You're welcome!",
                "Glad I could help!",
                "No problem at all!"
            ],
            
            # Capabilities
            r'\bcan you\b|\bhelp\b|\bdo for me\b': [
                "I can answer basic questions about: \n- Myself \n- The time and date \n- Basic calculations \nI can also chat about simple topics!",
                "As a simple rule-based chatbot, I can: \n- Respond to greetings \n- Tell you the time/date \n- Perform basic math \n- Answer questions about myself",
                "Type 'help' for a list of things I can respond to!"
            ],
            
            # Math operations
            r'calculate\s([\d\+\-\*\/\(\)\s\.]+)': [
                "The result is {result}.",
                "That equals {result}.",
                "Computing... the answer is {result}."
            ],
            
            # Feelings
            r'\blove you\b|\blike you\b': [
                "That's nice of you to say! I'm just a program, but I enjoy our conversation.",
                "Thank you! I'm here to be helpful.",
                "I appreciate that! I'm designed to be likable."
            ],
            
            # Joke
            r'\bjoke\b|\bfunny\b': [
                "Why don't scientists trust atoms? Because they make up everything!",
                "What's a computer's favorite snack? Microchips!",
                "Why did the chatbot go to therapy? It had too many issues to debug!"
            ]
        }
        
        # Store conversation history
        self.conversation_history = []
        
    def respond_to(self, user_input):
        # Store user input in conversation history
        self.conversation_history.append(("user", user_input))
        
        # Convert to lowercase for case-insensitive matching
        user_input_lower = user_input.lower()
        
        # Check for exit command first
        exit_pattern = r'\b(bye|goodbye|exit|quit)\b'
        if re.search(exit_pattern, user_input_lower):
            response = random.choice(self.patterns[exit_pattern])
            self.conversation_history.append(("bot", response))
            return response, True
        
        # Check for calculator function
        calc_match = re.search(r'calculate\s([\d\+\-\*\/\(\)\s\.]+)', user_input_lower)
        if calc_match:
            try:
                expression = calc_match.group(1)
                result = eval(expression)
                response_template = random.choice(self.patterns[r'calculate\s([\d\+\-\*\/\(\)\s\.]+)'])
                response = response_template.replace("{result}", str(result))
                self.conversation_history.append(("bot", response))
                return response, False
            except:
                response = "Sorry, I couldn't calculate that. Make sure your expression is valid."
                self.conversation_history.append(("bot", response))
                return response, False
        
        # Check for matches in other patterns
        for pattern, responses in self.patterns.items():
            if re.search(pattern, user_input_lower):
                response = random.choice(responses)
                self.conversation_history.append(("bot", response))
                return response, False
        
        # Default response if no pattern matches
        default_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "I don't have a response for that yet.",
            "I'm still learning and don't understand that query.",
            "Could you try asking something else?"
        ]
        response = random.choice(default_responses)
        self.conversation_history.append(("bot", response))
        return response, False
    
    def get_conversation_history(self):
        return self.conversation_history

    def thinking_animation(self, duration=1):
        """Display a thinking animation for the specified duration"""
        frames = [".  ", ".. ", "...", " ..", "  .", "   "]
        end_time = time.time() + duration
        
        while time.time() < end_time:
            for frame in frames:
                print(f"\rThinking{frame}", end="")
                time.sleep(0.2)
        print("\r" + " " * 12 + "\r", end="")

def run_chatbot():
    chatbot = RuleBasedChatbot()
    
    print("ChattyBot: Hello! I'm ChattyBot, a rule-based chatbot.")
    print("ChattyBot: You can chat with me about various topics or type 'bye' to exit.")
    
    exit_chat = False
    while not exit_chat:
        user_input = input("You: ")
        
        # Add a small delay and "thinking" animation to make the interaction feel more natural
        chatbot.thinking_animation(duration=random.uniform(0.5, 1.5))
        
        response, exit_chat = chatbot.respond_to(user_input)
        print(f"ChattyBot: {response}")
    
    # Optional: Display the conversation history at the end
    # print("\nConversation Summary:")
    # for speaker, message in chatbot.get_conversation_history():
    #     print(f"{speaker.capitalize()}: {message}")

if __name__ == "__main__":
    run_chatbot()