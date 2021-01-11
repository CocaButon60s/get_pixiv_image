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
        this.modal.showModal('IDエラー', 'ユーザーIDを入力してください', false, {color: 'secondary', label: '閉じる'})
        return
      }
      if (this.pswd === '') {
        this.modal.showModal('パスワードエラー', 'パスワードを入力してください', false, {color: 'secondary', label: '閉じる'})
        return
      }
      this.modal.showModal('ログイン中', 'しばらくお待ちください', true)

      // ログイン処理
      var result = await eel.login(this.id, this.pswd)()
      if (result === 'SUCCESS') {
        this.modal.hideModal()
        Router.push('/get_image')
      } else if (result === 'ERR:LOGIN') {
        this.modal.showModal('ログイン失敗', 'ユーザーDまたはパスワードが違います', false, {color: 'secondary', label: '閉じる'})
      } else {
        this.modal.showModal('内部エラー', '開発者に連絡してください', false, {color: 'secondary', label: '閉じる'})
      }
    }
  },
  components: {InputForm, ButtonForm}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
