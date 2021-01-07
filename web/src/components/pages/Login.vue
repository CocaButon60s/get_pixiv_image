<template>
  <div class="container-fluid form-group">
    <input-form :contents.sync="id">ユーザーID:</input-form>
    <input-form :contents.sync="pswd">password:</input-form>
    <button-form @callback="login" :isLoading="isLoading">
      ログイン
      <template v-slot:after-push>Loading...</template>
    </button-form>
  </div>
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
      pswd: '',
      isLoading: false
    }
  },
  mounted: async function () {
    var info = await eel.load_user_info()()
    this.id = info[0]
    this.pswd = info[1]
  },
  methods: {
    async login () {
      this.isLoading = true
      // パラメータチェック
      if (this.id === '') {
        await this.$bvModal.msgBoxOk('ユーザーIDを入力してください', {
          'title': 'IDエラー',
          'noCloseOnBackdrop': true,
          'okVariant': 'secondary',
          'okTitle': '閉じる'
        })
        this.isLoading = false
        return
      }
      if (this.pswd === '') {
        await this.$bvModal.msgBoxOk('パスワードを入力してください', {
          'title': 'パスワードエラー',
          'noCloseOnBackdrop': true,
          'okVariant': 'secondary',
          'okTitle': '閉じる'
        })
        this.isLoading = false
        return
      }

      // ログイン処理
      var result = await eel.login(this.id, this.pswd)()
      if (result === 'SUCCESS') {
        this.isLoading = false
        Router.push('/get_image')
      } else if (result === 'ERR:LOGIN') {
        await this.$bvModal.msgBoxOk('ユーザーIDまたはパスワードが違います', {
          'title': 'ログイン失敗',
          'noCloseOnBackdrop': true,
          'okVariant': 'secondary',
          'okTitle': '閉じる'
        })
        this.isLoading = false
      } else {
        await this.$bvModal.msgBoxOk('開発者に連絡してください', {
          'title': '内部エラー',
          'noCloseOnBackdrop': true,
          'okVariant': 'secondary',
          'okTitle': '閉じる'
        })
        this.isLoading = false
      }
    }
  },
  components: {InputForm, ButtonForm}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
