import emoji


print(f'Emojis disponíveis: {emoji.emojize(':red_heart:')} - :red_heart:')
print(f'Emojis disponíveis: {emoji.emojize(':thumbs_up:')} - :thumbs_up:')
print(f'Emojis disponíveis: {emoji.emojize(':thinking_face:')} - :thinking_face:')
print(f'Emojis disponíveis: {emoji.emojize(':partying_face:')} - :partying_face:')

frase = input('Digite uma frase e ela será emojizada: ')
fraseEmojizada = emoji.emojize(frase)
print(f'Frase emojizada: {fraseEmojizada}')