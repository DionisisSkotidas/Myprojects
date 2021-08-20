abc = 'a b c d e f g h i j k l m o n p q r s t u v w x y z ' \
      'a b c d e f g h i j k l m o n p q r s t u v w x y z ' \
      'a b c d e f g h i j k l m o n p q r s t u v w x y z ' \
      'a b c d e f g h i j k l m o n p q r s t u v w x y z ' \
      'a b c d e f g h i j k l m o n p q r s t u v w x y z ' \
      'a b c d e f g h i j k l m o n p q r s t u v w x y z ' \
      'a b c d e f g h i j k l m o n p q r s t u v w x y z ' \
      'a b c d e f g h i j k l m o n p q r s t u v w x y z ' \
      'a b c d e f g h i j k l m o n p q r s t u v w x y z '
alphabet = abc.split()
# print(alphabet)


def encryption(input_text, shift=1):
    input_text.lower()
    output_text = ''
    for letter in input_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            encrypted_position = position + shift
            output_text += alphabet[encrypted_position]
        else:
            output_text += letter
    return output_text


def decryption(input_text, shift=1):
    input_text.lower()
    output_text = ''
    for letter in input_text:
        if letter in alphabet:
            position = alphabet.index(letter) + 26
            decrypted_position = position - shift
            output_text += alphabet[decrypted_position]
        else:
            output_text += letter
    return output_text


if __name__ == '__main__':
    trial = 'hello there'
    en_trial = encryption(input_text=trial, shift=3)
    print(en_trial)
    de_trial = decryption(input_text=en_trial, shift=3)
    print(de_trial)
