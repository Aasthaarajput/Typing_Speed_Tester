import time
import random

def typing_speed_test():

    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a fun programming language to learn.",
        "Typing speed tests are a great way to improve your skills.",
        "Artificial Intelligence is shaping the future of technology.",
        "Consistency is the key to mastering any skill."
    ]

    print("\n--- Typing Speed Tester ---")
    print("Type the sentence shown as fast as you can.")
    print("Press Enter when you're ready to start.\n")

    total_time = 0
    total_wpm = 0
    total_accuracy = 0
    rounds = 0

    while True:

        sentence = random.choice(sentences)
        input("Press Enter to start the round...")
        print("\nType this sentence:")
        print(f"--> {sentence}\n")

        start_time = time.time()

        typed_sentence = input("\nYour input: ")

        end_time = time.time()

        time_taken = end_time - start_time
        words_per_minute = (len(typed_sentence.split()) / time_taken) * 60
        accuracy = calculate_accuracy(sentence, typed_sentence)

        total_time += time_taken
        total_wpm += words_per_minute
        total_accuracy += accuracy
        rounds += 1

        print("\n--- Round Results ---")
        print(f"Time Taken: {time_taken:.2f} seconds")
        print(f"Words Per Minute (WPM): {words_per_minute:.2f}")
        print(f"Accuracy: {accuracy:.2f}%\n")

        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    print("\n--- Overall Score ---")
    print(f"Total Rounds Played: {rounds}")
    print(f"Average WPM: {total_wpm / rounds:.2f}")
    print(f"Average Accuracy: {total_accuracy / rounds:.2f}%")
    print(f"Total Time Spent: {total_time:.2f} seconds\n")
    print("Thanks for playing! Goodbye!")


def calculate_accuracy(original, typed):
    """Calculate the accuracy percentage between original and typed text."""
    original_words = original.split()
    typed_words = typed.split()

    correct_words = sum(1 for o, t in zip(original_words, typed_words) if o == t)
    total_words = len(original_words)

    accuracy = (correct_words / total_words) * 100
    return accuracy


if __name__ == "__main__":
    typing_speed_test()
