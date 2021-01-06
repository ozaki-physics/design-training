import requests
import os

def get_search_tag_text(get_url_info, search_text):
  """
  get_url_info 取得したhtml情報
  search_text 探したいhtmlタグ
  戻り値は search_text の中の要素
  """
  tag_start = get_url_info.text.find("<"+search_text+">")
  tag_end = get_url_info.text.find("</"+search_text+">")
  tag_start += 2 + len(search_text)
  return (get_url_info.text[tag_start:tag_end])

def write_text(write_file_name, text):
  """
  ファイルに text を書き込み 最後に改行する
  追記モード, UTF-8, 改行コードはLF
  """
  with open(write_file_name, mode="a", encoding="utf-8", newline="") as file_wr:
      file_wr.write(text + "\n")

def add_brackets(text):
  return "(" + text + ")"

def main():
  """
  file_name が読み込ませたいファイル名(同じディレクトリ内)
  write_file_name が書き出したいファイル名
  書き出した後 VSCode の機能を使って html にして読む
  読み込みファイルの行にhttpという文字が入っていたらタイトルを取りに行く
  """
  # プログラム的に使う変数
  j = 0

  # 必要に応じて変える変数
  search_text = "title"
  base_path = os.path.dirname(__file__)
  file_name = base_path + "/refarences01-memo.md"
  write_file_name = base_path + "/refarences.md"
  progress_comment = "今{0}行目を実行中です"

  with open(file_name, mode="r", encoding="utf-8") as file_re:
    for one_line in file_re:
      # フォーマットに値を代入するだけ
      print(progress_comment.format(str(j+1).zfill(4)))
      # httpという文字列が含まれているか
      if one_line.find("http") != -1:
        # 改行文字を取り除く
        url = one_line.replace("\n","")
        # htmlを取得
        get_url_info = requests.get(url)
        # ステータスコードが正常で 探したい文字列が見つかった
        if get_url_info.status_code == 200 and get_url_info.text.find(search_text) != -1:
          save_text = "<a href=\"" + url + "\" target=\"_blank\">" + get_search_tag_text(get_url_info, search_text) + "</a><br>"
          write_text(write_file_name, save_text)
      j += 1

if __name__ == "__main__":
  main()
