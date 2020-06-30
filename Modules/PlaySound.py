import winsound


def Start():
    print('Play SystemHand sound')
    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
