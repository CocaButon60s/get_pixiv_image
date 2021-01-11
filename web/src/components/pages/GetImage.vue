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
  data: function () {
    return { id: '' }
  },
  props: ['modal'],
  methods: {
    async get_image () {
      // パラメータチェック
      if (this.id === '') {
        this.modal.showModal('IDエラー', '画像を取得するユーザーのIDを入力してください', false, {color: 'secondary', label: '閉じる'})
        return
      }
      this.modal.showModal('画像取取得中', 'しばらくお待ちください', true, {color: 'danger', label: '閉じる'})

      // 画像取得
      var result = await eel.get_image(this.id)()
      if (result === 'SUCCESS') {
        this.modal.showModal('画像取得成功', 'imagesフォルダ内を確認してください', false, {color: 'secondary', label: '閉じる'})
      } else {
        this.modal.showModal('画像取得失敗', 'IDを確認してください', false, {color: 'secondary', label: '閉じる'})
      }
    }
  },
  components: {InputForm, ButtonForm}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
