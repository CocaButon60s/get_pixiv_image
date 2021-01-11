<template>
  <b-modal v-model="isShown" :noCloseOnBackdrop="true" :no-stacking="true">
    <template #modal-title>{{ title }}</template>
    <template #default>
      <b-container fluid>
        <b-row>
          <b-col cols="1" v-show="isLoading"><b-spinner label="Spinning"></b-spinner></b-col>
          <b-col>{{ content }}</b-col>
        </b-row>
      </b-container>
    </template>
    <template #modal-footer>
      <b-button :variant="okColor" v-show="isShownOK" @click="ok()">{{ okLabel }}</b-button>
    </template>
  </b-modal>
</template>

<script>
export default {
  name: 'ModalForm',
  data: function () {
    return {
      title: '',
      isLoading: false,
      isShownOK: true,
      content: '',
      okColor: 'secondary',
      okLabel: '閉じる',
      isShown: false
    }
  },
  methods: {
    showModal (title, isLoading, content, okColor, okLabel) {
      this.title = title
      this.isLoading = isLoading
      this.content = content
      this.okColor = (typeof (okColor) !== 'undefined' ? okColor : 'secondary')
      this.isShownOK = (typeof (okLabel) !== 'undefined')
      this.okLabel = (typeof (okLabel) !== 'undefined' ? okLabel : '')
      this.isShown = true
    },
    hideModal () { this.isShown = false },
    setOkProc (func) { this.ok = func },
    ok () { this.hideModal() }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
