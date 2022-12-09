def encryption():
    import matplotlib.pyplot as plt
    import numpy as np

    global user_key, user_text, num


    user_text = input()

    user_key = input()
    # n is the no: of bits to be considered at a time
    num = int(input())

    print("Plain text : ", user_text)
    print("Key : ", user_key)
    print("n : ", num)

    print(" ")


    S = [i for i in range(0, 2 ** num)]
    print("S : ", S)

    key_list = [user_key[i:i + num] for i in range(0, len(user_key), num)]


    for i in range(len(key_list)):
        key_list[i] = int(key_list[i], 2)


    global pt

    pt = [user_text[i:i + num] for i in range(0, len(user_text), num)]

    for i in range(len(pt)):
        pt[i] = int(pt[i], 2)



    diff = int(len(S) - len(key_list))

    if diff != 0:
        for i in range(0, diff):
            key_list.append(key_list[i])

    print("Key list : ", key_list)
    print(" ")

    def KSA():
        j = 0
        N = len(S)

        for i in range(0, N):
            j = (j + S[i] + key_list[i]) % N

            S[i], S[j] = S[j], S[i]
            print(i, " ", end="")

            print(S)

            initial_permutation_array = S

            print("The initial permutation array is : ",
                  initial_permutation_array)

    KSA()

    def PGRA():

        N = len(S)
        i = j = 0
        global key_stream
        key_stream = []

        for k in range(0, len(pt)):
            i = (i + 1) % N
            j = (j + S[i]) % N

            S[i], S[j] = S[j], S[i]
            print(k, " ", end="")

            t = (S[i] + S[j]) % N
            key_stream.append(S[t])

            print("Key stream : ", key_stream)
            print(" ")
        plt.plot(np.array(range(0, len(pt))), np.array(key_stream))

        plt.show()

    print("PGRA iterations : ")
    print(" ")
    PGRA()

    def XOR():
        global cipher_text
        cipher_text = []
        for i in range(len(pt)):
            c = key_stream[i] ^ pt[i]
            cipher_text.append(c)

    XOR()

    encrypted_to_bits = ""
    for i in cipher_text:
        encrypted_to_bits += '0' * (num - len(bin(i)[2:])) + bin(i)[2:]

    print("Cipher : ", encrypted_to_bits)


encryption()

print("---------------------------------------------------------")


def decryption():
    def do_XOR():
        global original_text
        original_text = []
        for i in range(len(cipher_text)):
            p = key_stream[i] ^ cipher_text[i]
            original_text.append(p)

    do_XOR()

    decrypted_to_bits = ""
    for i in original_text:
        decrypted_to_bits += '0' * (num - len(bin(i)[2:])) + bin(i)[2:]

    print(" ")
    print("Decrypted : ",
          decrypted_to_bits)


decryption()
