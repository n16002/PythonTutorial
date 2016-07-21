HANDS = ['グー', 'チョキ', 'パー']


def select_hand():
    """
    コンピュータの手をランダムに決める
    :return: HANDSの中のいずれか。
    """
    import random
    random.choice(HANDS)

    return


def judgement(player, computer):
    """
    じゃんけんの勝敗を判定する。
    :param player: HANDSの中のどれか
    :param computer: HANDSの中のどれか
    :return: プレイヤーが勝ちの場合は１、あいこは０。負けは−１を返す
    """
    pass

def save_score(result):
    """
    'score.txt'に戦績を保存。
    win:x lose:y draw:zのディクショナリデータを保存する。
    :param result:
    :return: None
    """
    a = open("score.txt", "w")

    res = {'win': x, 'lose': y, 'draw': z}

    a.write(res)

    a.close()

    return


if __name__ == '__main__':
    player = int(input('グー(1)/チョキ(2)/パー(3)を選んでください(数字): '))
    computer = select_hand()
    result = judgement(player, computer)
    # コンピュータの手と勝敗の結果を表示
    print(computer)
    print(result)

    save_score(result)
