<template>
  <b-container fluid class="form-group">
    <input-form :contents.sync="id">ユーザーID:</input-form>
    <input-form :contents.sync="pswd">password:</input-form>
    <button-form @callback="login">ログイン</button-form>
  </b-container>
</template>

<script>
import InputForm from '@/components/parts/InputForm'
import ButtonForm from '@/components/parts/ButtonForm'
import Router from '@/router/index'
export default {
  name: 'Login',
  data: function () {
    return {
      id: '',
      pswd: ''
    }
  },
  props: ['modal'],
  mounted: async function () {
    var info = await eel.load_user_info()()
    this.id = info[0]
    this.pswd = info[1]
  },
  methods: {
    async login () {
      // パラメータチェック
      if (this.id === '') {
        this.modal.showModal('IDエラー', false, 'ユーザーIDを入力してください', 'secondary', '閉じる')
        return
      }
      if (this.pswd === '') {
        this.modal.showModal('パスワードエラー', false, 'パスワードを入力してください', 'secondary', '閉じる')
        return
      }
      this.modal.showModal('ログイン中', true, 'しばらくお待ちください')

      // ログイン処理
      var result = await eel.login(this.id, this.pswd)()
      if (result === 'SUCCESS') {
        this.modal.hideModal()
        Router.push('/get_image')
      } else if (result === 'ERR:LOGIN') {
        this.modal.showModal('ログイン失敗', false, 'ユーザーDまたはパスワードが違います', 'secondary', '閉じる')
      } else {
        this.modal.showModal('内部エラー', false, '開発者に連絡してください', 'secondary', '閉じる')
      }
    }
  },
  components: {InputForm, ButtonForm}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
