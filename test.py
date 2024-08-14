import MeCab

def test_mecab():
    # テストするテキスト
    text = "こんにちは、世界！これはMeCabのテストです。"

    # MeCabのTaggerオブジェクトを作成
    tagger = MeCab.Tagger("-Owakati")

    # テキストを分かち書き
    result = tagger.parse(text)

    # 結果を表示
    print("入力テキスト: ", text)
    print("分かち書き結果: ", result)

if __name__ == "__main__":
    test_mecab()
