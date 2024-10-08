# A short adventure game in the shattered realm

print("Welcome to the Shattered Realm")
userName = input("Input your name: ")
print(f'Welcome, {userName}, brave adventurer! Your journey begins at the Crossroads of Fate.\n'
      "Your goal is to get a magical artifact. If you cannot, YOU LOSE!\n"
      "1. Forest of Whispers\n"
      "2. Cavern of Echoes\n"
      "3. Plains of Illusions")
pathChoice = int(input(f"{userName}, which way you want to go? (1, 2, or 3): "))

if pathChoice == 1:
    print("You have entered the Forest of Whispers and have encountered a glowing crystal.")
    crystalChoice = input('Do you want to touch the crystal or ignore it? (Touch or Ignore): ').lower()
    if crystalChoice == 'touch':
        courageValue = int(input('How courageous are you today? (1-10): '))
        if courageValue < 5:
            print("You are not brave :(\n"
                  "You run out of the cave\n"
                  "----You Lose!!----")
        else:
            print('It turns out inside the glowing crystal was a magical artifact\n'
                  "You gain a magical artifact\n"
                  "----You Win!!----")
    else:
        print("You stumble into a trap and die\n"
              "----You Lose!!---")
elif pathChoice == 2:
    print("You have entered the Cavern of Echoes\n"
          "A floating orb asks you to reveal a secret")
    orbChoice = input("Whisper a secret or share a rumor (secret, rumor): ").lower()
    if orbChoice == 'secret':
        print("The orb is satisfied with your secret\n"
              "You are granted a magical artifact\n"
              "----You Win!!----")
    else:
        escapeNumber = float(input("The orb laughs and traps you. Enter any number between 1 and 20 to escape"))
        if escapeNumber < 10.1:
            print("You are smart and receive a magical artifact\n----You Win!!----")
        else:
            print("The orb has successfully trapped you for eternity\n----You Lose!!----")
else:
    print("You have entered the plains of Illusions")
    print("You are confronted by an illusionist")
    illusionChoice = input("Choose a path: Trust your gut feeling or analyze the illusions (gut, analyze): ").lower()
    if illusionChoice == 'gut':
        print("You take a deep breath, closing your eyes to focus on your instincts.\n"
              "You point towards a shimmering path.\n"
              "The illusionist nods approvingly, and the path before you solidifies.\n"
              "......")
        illusionNumber = int(input("You encounter a series of illusions that try to deceive you, you must choose a number 1-6: "))
        if illusionNumber == 5:
            print("You safely navigate through illusions and find a magical artifact\n"
                  "----You Win!!----")
        elif illusionNumber > 6:
            print('The illusionist says "You are trickier than me. Well done!"')
            print("The illusionist gives you a magical artifact.\n"
                  '----You Win!!----')
        else:
            print("You become trapped in an illusion for eternity\n"
                  '----You Lose!!----')
    else:
        print("You take a moment o observe your surroundings.\n"
              "Patterns emerge, and you start to discern the real from the fake.\n"
              "The illusionist looks impressed.\nThe illusionist instead asks a riddle.\n"
              "I am a number between one and two,\n"
              "A fraction of light, shining through.\n"
              "If you take half of me, you'll find,\n"
              "A piece of a whole, both gentle and kind")
        riddleNumber = float(input("What am I?"))
        if riddleNumber == 1.5:
            print("You have answered the illusionists riddle correctly and recieve a magical artifact as reward.\n"
                  "----You Win!!----")
        else:
            print("You have become trapped in the illusion for all eternity :(\n"
                  "----You Lose!!----")