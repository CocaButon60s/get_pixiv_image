// ローディング制御
function ctrl_loading(page, is_loading) {
  $(page + " button").prop("disabled", is_loading)
  $(page + " button .text").css("display", is_loading ? "none":"block")
  $(page + " button .spinner").css("display", is_loading ? "block":"none")
}
// モーダル制御
function ctrl_modal(title, msg, ok_btn_is_shown) {
  $("#modal .modal-title").text(title)
  $("#modal .modal-body").text(msg)
  $("#modal .btn-primary").css("display", ok_btn_is_shown ? "block":"none")
  $("#modal").modal("show")
}
// 画像取得画面
function change_page(from, to) {$(from).hide(); $(to).show();}

// ログイン
async function login() {
  var id = $("#login .id").val()
  var pswd = $("#login .pswd").val()
  if (id=="") {ctrl_modal("IDエラー", "Pixiv IDを入力してください", false); return;}
  if (pswd=="") {ctrl_modal("パスワードエラー", "パスワードを入力してください", false); return;}

  // ログイン処理
  var result = await eel.login(id, pswd)()
  if (result === "SUCCESS") {change_page("#login", "#get_image")}
  else if (result === "ERR:LOGIN") {ctrl_modal("ログインエラー", "IDまたはパスワード違います", false)}
  else {ctrl_modal("内部エラー", "作成者に連絡ください", false)}
}
// 画像を取得する
async function get_image() {
  var id = $("#get_image .id").val()
  if (id=="") {ctrl_modal("IDエラー", "画像を取得するユーザのIDを入力してください", false); return;}

  var result = await eel.get_image(id)()
  if (result === "SUCCESS") {ctrl_modal("取得成功", "imagesフォルダ内を確認してください", false)}
  else {ctrl_modal("取得失敗", "再度取得を実行してください", false)}
}
// モーダルのボタン設定
function set_modal_btn(page) {
  ctrl_loading(page, true)
  // モーダルのボタンの設定
  $("#modal .btn-secondary").click(function() {
    $("#modal .btn-secondary").off("click")
    ctrl_loading(page, false)
  })
}
// ユーザー情報を読込む
async function load_user_info() {
  var info = await eel.load_user_info()()
  $("#login .id").val(info[0])
  $("#login .pswd").val(info[1])
}
$(function() {
  load_user_info()
  // ログイン画面
  // ログインボタンの設定
  $("#login button").click(function() {
    set_modal_btn("#login")
    login()
  })
  // 画像取得画面
  $("#get_image button").click(function() {
    set_modal_btn("#get_image")
    get_image()
  })
})