//data
let arr = [
  ["user_name", "氏名", ["テキスト"]],
  ["mail_address", "メールアドレス", ["テキスト"]],
  ["sex", "性別", ["男", "女", "どちらでもない"]],
  ["tel", "電話番号", ["テキスト"]],
  ["postal_code", "郵便番号", ["テキスト"]],
  ["address", "住所", ["全国", "北海道", "青森県", "岩手県県", "宮城県", "秋田県", "山形県", "福島県", "茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県", "新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県", "岐阜県", "静岡県", "愛知県", "三重県", "滋賀県", "京都府", "大阪府", "兵庫県", "奈良県", "和歌山県", "鳥取県", "島根県", "岡山県", "広島県", "山口県", "徳島県", "香川県", "愛媛県", "高知県", "福岡県", "佐賀県", "長崎県", "熊本県", "大分県", "宮崎県", "鹿児島県", "沖縄県"]],
  // ["join_date" ,"登録日", [""]]
  // ["" ,"最終更新日", []]

  // ["target_sex","性別",["男性","女性","どちらも"]],
  // ["target_age","年齢",["0～9歳","10～19歳","20～29歳","30～39歳","40～49歳","50～59歳","60～69歳","70歳以上"]],
  // ["keyword","キーワード",["テキスト"]],
  // ["campaign_period","キャンペーン期間",["---------------","今月","来月","再来月以降"]],
  // ["price","希望価格",['---------------',"50,000～100,000円","100,000～150,000円","150,000～200,000円","200,000～250,000円","250,000～300,000円","300,000～350,000円","350,000～400,000円","400,000～450,000円","450,000～500,000円","500,000円以上"]],
  // ["hope_category","希望カテゴリー",['---------------','週刊誌','男性誌','女性誌','総合情報','モノ・トレンド','ビジネス・マネー','料理・グルメ・レシピ','美容・コスメ','健康情報','マタニティ・育児','幼児・子供','エリア情報','旅行・レジャー','テレビ情報','スポーツ','コミック','ゲーム・アニメ情報','趣味・専門','その他',]],
  // ["ng_category","NGカテゴリー",['---------------','週刊誌','男性誌','女性誌','総合情報','モノ・トレンド','ビジネス・マネー','料理・グルメ・レシピ','美容・コスメ','健康情報','マタニティ・育児','幼児・子供','エリア情報','旅行・レジャー','テレビ情報','スポーツ','コミック','ゲーム・アニメ情報','趣味・専門','その他',]],
  // ["area","エリア",["全国","北海道","青森","岩手","宮城","秋田","山形","福島","茨城","栃木","群馬","埼玉","千葉","東京","神奈川","新潟","富山","石川","福井","山梨","長野","岐阜","静岡","愛知","三重","滋賀","京都","大阪","兵庫","奈良","和歌山","鳥取","島根","岡山","広島","山口","徳島","香川","愛媛","高知","福岡","佐賀","長崎","熊本","大分","宮崎","鹿児島","沖縄"]],
]

//初期表示
let y
let selector = document.getElementById('selector')
for (let i = 0; i < arr.length; i++) {
  let element = document.createElement('option')
  element.innerText = arr[i][1]
  element.setAttribute("value", i)
  element.setAttribute("name", arr[i][0])
  selector.appendChild(element)
}

//プルダウン変更時
const searchFunc = (e) => {
  //2番目プルダウンを一度削除する
  let secondSelector = document.getElementById('secondSelector')
  let output = document.getElementById('output')
  secondSelector.removeChild(output)
  //「未選択」の場合
  if (e == 101) {
    console.log('未選択-==================')
    let submit = document.getElementById('submit')
    // submit.setAttribute("disabled", "true")
    //削除したselectタグを作り直す
    let output = document.createElement('select')
    output.setAttribute('id', "output")
    output.setAttribute('name', "output")
    output.setAttribute("class", "form-control")
    secondSelector.appendChild(output)
    return
  }

  //selectタグを作成する
  let parent
  if (arr[e][2][0] == "テキスト") {
    parent = document.createElement("input")
    parent.setAttribute("type", "text")
    parent.setAttribute("id", "output")
    parent.setAttribute("name", "output")
    parent.setAttribute("class", "form-control")
  } else {
    console.log('未選択===============2')
    parent = document.createElement("select")
    parent.setAttribute("id", "output")
    parent.setAttribute("name", "output")
    parent.setAttribute("class", "form-control")
    //一時配列e番目の2要素目配列を全て加える
    arr[e][2].forEach((element, index) => {
      let child = document.createElement("option")
      if (arr[e][1] == "キャンペーン期間") {
        child.setAttribute("value", (arr[e][0].indexOf("campaign_period") != -1) ? index : element)
      } else if (arr[e][1] == "希望価格") {
        child.setAttribute("value", (arr[e][0].indexOf("price") != -1) ? index : element)
      } else if (arr[e][1] == "希望カテゴリー" | arr[e][1] == "NGカテゴリー") {
        child.setAttribute("value", (arr[e][0].indexOf("category") != -1) ? index : element)
      }
      parent.setAttribute("class", "sch-selector form-control")
      child.setAttribute("name", element)
      child.innerText = element
      parent.appendChild(child)
    })
  }
  secondSelector.appendChild(parent)
  let submit = document.getElementById('submit')
  submit.removeAttribute("disabled")
}



//■スライドショー機能
class PageBlock {
  constructor(classes, location) {
    this.classes = classes
    this.location = location
    this.page = 1
    this.itemPerPage = 3
    this.minItem = 0
    this.maxItem = this.itemPerPage - 1
    this.elements = document.getElementsByClassName(this.classes)
    this.items = this.elements.length
    this.maxPage = Math.ceil(this.items / this.itemPerPage)
    this.pageInfo = document.getElementById(this.location)
    this.initialize()
  }
  initialize() {
    let elements = document.getElementsByClassName(this.classes)
    for (let i = 0; i < elements.length; i++) {
      elements[i].setAttribute("id", this.classes + i)
    }
  }
  scroll(num) {
    if ((this.page + num) > this.maxPage || (this.page + num) < 1) {
      return
    }
    this.page += num
    this.minItem = (this.page == 1) ? 0 : this.page * this.itemPerPage - this.itemPerPage
    this.maxItem = (this.page == 1) ? this.itemPerPage - 1 : this.page * this.itemPerPage - 1
    this.render()
  }
  render() {
    for (let i = 0; i < this.elements.length; i++) {
      if (i <= this.maxItem && i >= this.minItem) {
        this.elements[this.classes + i].setAttribute("class", this.classes)
      } else {
        this.elements[this.classes + i].setAttribute("class", "block detail " + this.classes)
      }
    }
    this.pageInfo.innerText = `ページ数:${this.page}/${this.maxPage}`
  }
}
const firstBlock = new PageBlock("campAndMag", "pageInfo")
firstBlock.render()
const secondBlock = new PageBlock("productAndCampaign", "pageInfoSecond")
secondBlock.render()

function scroll(num) {
  firstBlock.scroll(num)
}
function scroll2(num) {
  secondBlock.scroll(num)
}