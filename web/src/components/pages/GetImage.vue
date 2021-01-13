<template>
  <b-container fluid class="form-group">
    <input-form :contents.sync="id">Pixiv ID:</input-form>
    <button-form @callback="get_image">取得</button-form>
  </b-container>
</template>

<script>
import InputForm from '@/components/parts/InputForm'
import ButtonForm from '@/components/parts/ButtonForm'
export default {
  name: 'GetImage',
  data: function () { return {id: ''} },
  props: ['modal'],
  methods: {
    async get_image () {
      // パラメータチェック
      if (this.id === '') {
        this.modal.showModal('IDエラー', '画像を取得するユーザーのIDを入力してください', false, {color: 'secondary', label: '閉じる'})
        return
      }
      this.modal.showModal('画像取取得中', 'しばらくお待ちください', true, {color: 'danger', label: '中止', cb: this.cancel})
      // 画像取得
      await eel.py_set_target(this.id)()
      var timer = setInterval(async () => {
        var result = await eel.py_get_image()()
        if (result === 'CONTINUE') return
        if (result === 'SUCCESS') this.modal.showModal('画像取得成功', 'imagesフォルダ内を確認してください', false, {color: 'secondary', label: '閉じる'})
        if (result === 'CANCEL') this.modal.showModal('画像取得中止', '画像取得を中止しました', false, {color: 'secondary', label: '閉じる'})
        if (result === 'ERR') this.modal.showModal('画像取得失敗', 'IDを確認してください', false, {color: 'secondary', label: '閉じる'})
        clearInterval(timer)
      }, 2000)
    },
    async cancel () { await eel.py_cancel()() }
  },
  components: {InputForm, ButtonForm}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
