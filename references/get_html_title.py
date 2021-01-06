import requests
import os
from bs4 import BeautifulSoup

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

def get_search_tag_text2(get_url_info, search_text):
  soup = BeautifulSoup(get_url_info.text, "html.parser")
  return soup.find(search_text).get_text()

def write_text(write_file_name, text):
  """
  ファイルに text を書き込み 最後に改行する
  追記モード, UTF-8, 改行コードはLF
  """
  with open(write_file_name, mode="a", encoding="utf-8", newline="") as file_wr:
      file_wr.write(text + "\n")

def add_brackets(text):
  return "(" + text + ")"

def get_html_title(url, search_text):
  # htmlを取得
  get_url_info = requests.get(url)
  # ステータスコードが正常で 探したい文字列が見つかった
  if get_url_info.status_code == 200 and get_url_info.text.find(search_text) != -1:
    save_text = "<a href=\"{0}\" target=\"_blank\">{1}</a><br>".format(url, get_search_tag_text(get_url_info, search_text))
  return save_text

def replacement_md_title(url, search_text):
  save_text = url
  # a閉じタグが見つかったらタイトルを取得し終わっているからそのまま返す
  if url.find("</a>") != -1:
    return save_text
  # htmlを取得
  get_url_info = requests.get(url)
  # ステータスコードが正常で 探したい文字列が見つかった
  if get_url_info.status_code == 200 and get_url_info.text.find(search_text) != -1:
    save_text = "<a href=\"{0}\" target=\"_blank\" alt=\"{0}\">{1}</a>".format(url, get_search_tag_text2(get_url_info, search_text))
  return save_text

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
        save_text = get_html_title(url, search_text)
        write_text(write_file_name, save_text)
      j += 1

def main2():
  """
  file_name が読み込ませたいファイル名(同じディレクトリ内)
  write_file_name が書き出したいファイル名
  書き出した後 VSCode の機能を使って html にして読む
  読み込みファイルの行にhttpという文字が入っていたらタイトルを取りに行く
  文の中に url が含まれている場合は正常に動作しない
  """
  # プログラム的に使う変数
  j = 0

  # 必要に応じて変える変数
  search_text = "title"
  base_path = os.path.dirname(__file__)
  file_name = base_path + "/references-memo.md"
  write_file_name = base_path + "/references.md"
  progress_comment = "今{0}行目を実行中です"

  with open(write_file_name, mode="w", encoding="utf-8") as file_wr:
    with open(file_name, mode="r", encoding="utf-8") as file_re:
      for one_line in file_re:
        # フォーマットに値を代入するだけ
        print(progress_comment.format(str(j+1).zfill(4)))
        # 改行文字を取り除く
        one_line = one_line.replace("\n","")
        # httpという文字列が含まれているか
        if one_line.find("http") != -1:
          one_line = replacement_md_title(one_line, search_text)
        file_wr.write(one_line + "<br>" + "\n")
        j += 1

if __name__ == "__main__":
  main2()
