<template>
  <div class="container-fluid form-group">
    <input-form :contents.sync="id">Pixiv ID:</input-form>
    <button-form @callback="get_image" :isLoading="isLoading">
      取得
      <template v-slot:after-push>取得中</template>
    </button-form>
  </div>
</template>

<script>
import InputForm from '@/components/parts/InputForm'
import ButtonForm from '@/components/parts/ButtonForm'
export default {
  name: 'GetImage',
  data: function () {
    return {
      id: '',
      isLoading: false
    }
  },
  methods: {
    async get_image () {
      this.isLoading = true
      // パラメータチェック
      if (this.id === '') {
        await this.$bvModal.msgBoxOk('画像を取得するユーザーのIDを入力してください', {
          'title': 'IDエラー',
          'noCloseOnBackdrop': true,
          'okVariant': 'secondary',
          'okTitle': '閉じる'
        })
        this.isLoading = false
        return
      }

      // 画像取得
      var result = await eel.get_image(this.id)()
      if (result === 'SUCCESS') {
        await this.$bvModal.msgBoxOk('imagesフォルダ内を確認してください', {
          'title': '画像取得成功',
          'noCloseOnBackdrop': true,
          'okVariant': 'secondary',
          'okTitle': '閉じる'
        })
      } else {
        await this.$bvModal.msgBoxOk('画像を取得するユーザーのIDを確認してください', {
          'title': '画像取得失敗',
          'noCloseOnBackdrop': true,
          'okVariant': 'secondary',
          'okTitle': '閉じる'
        })
      }
      this.isLoading = false
    }
  },
  components: {InputForm, ButtonForm}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
