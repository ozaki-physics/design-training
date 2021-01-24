## これが公式っぽい
https://developer.mozilla.org/ja/docs/Web/CSS/CSS_Grid_Layout/Basic_Concepts_of_Grid_Layout
## 用語
### コンテナ
グリッド全体を囲む要素
`display: grid;`または`display: inline-grid;`を指定することで その要素は Grid Layout のコンテナになる
### アイテム
コンテナの直接の子要素
```html
<div style="display:grid;"> <!-- コンテナ -->
    <div></div> <!-- アイテム-->
    <p></p> <!-- アイテム -->
    <section> <!-- アイテム -->
        <div></div> <!-- アイテムではない -->
    </section>
</div>
```
### トラック
グリッドの行および列のこと
言い換えれば 隣接する2本のラインの間のこと

### 単位 fr とは
https://developer.mozilla.org/ja/docs/Web/CSS/CSS_Grid_Layout/Basic_Concepts_of_Grid_Layout#the_fr_unit
グリッドには 柔軟なグリッドトラックを作成できるようにするため 追加の長さの単位が導入されています。
新しい fr 単位は グリッドコンテナー内の利用可能な空間の分数(a fraction)を表します。
1トラックを 分割した何個のグリッドとするかとか

### repeat()
https://developer.mozilla.org/ja/docs/Web/CSS/CSS_Grid_Layout/Basic_Concepts_of_Grid_Layout#track_listings_with_repeat_notation
grid-template-columns: 1fr 1fr 1fr;
grid-template-columns: repeat(3, 1fr);
は同じ意味を持つ
repeat(3, 2fr);はすべて2frになるから意味をなさない

### セル間隔
https://developer.mozilla.org/ja/docs/Web/CSS/CSS_Grid_Layout/Basic_Concepts_of_Grid_Layout#gutters
グリッドセル間の 溝 (Gutters) または 小路 (alleys) は column-gap および row-gap プロパティを使用するか、短縮プロパティの gap で作成できます。
column-gap と grid-column-gap の違いは グリッドレイアウトが導入された歴史的背景であり
ブラウザーは接頭辞を外すよう更新されつつある

### グリッドの自動配置 `grid-auto-flow: [ row | column ] || dense`
https://developer.mozilla.org/en-US/docs/Web/CSS/grid-auto-flow
row は横並び
column は縦並び
row dense は横並びで隙間があれば上から埋めていく
